import threading
import logging
import socket

import signal
import time

import config
import sys
import json
import copy
from threading import Thread, Lock
import asyncio
import netstruct

# global variables
exit_me = False
query_thread_exited = False
convergence_achieved = False
mutex = Lock()
num_client_exited = 0
network_state = {}
network_state_version = 1


def log_me(msg):
    logging.info(msg)


def exit_gracefully(sig, frame):
    global exit_me
    log_me('You pressed Ctrl+C!')
    exit_me = True

waiters = []

async def update_async_client(address, port, loop):
    global exit_me
    global convergence_achieved
    global network_state
    global network_state_version
    global waiters

    done = False

    my_network_state_version = -1

    while not done and not exit_me:

        try:
            log_me("Client : Making connection on {}:{}".format(address, port))
            reader, writer = await asyncio.open_connection(address, port,
                                                           loop=loop)

            while not exit_me:

                if convergence_achieved:
                    done = True

                log_me("Client: my network state {}".format(my_network_state_version))

                if my_network_state_version != network_state_version:
                    send_payload = json.dumps(network_state)
                else:

                    if done:
                        log_me("Client: CONVERGENCE achieved in client {}:{}".format(address, port))
                        break

                    fut = loop.create_future()
                    waiters.append(fut)
                    log_me("Client: Waiting on Change in state {} {}".format(address, port))
                    await fut
                    log_me("Client: Waiting OVER!! {} {}".format(address, port))
                    continue

                log_me('Client: Send: %r' % send_payload)
                try:
                    send_p = netstruct.pack(b"h$", send_payload.encode())
                    writer.write(send_p)
                    await writer.drain()
                except Exception as ex:
                    log_me("Client : Write Failed Error : {} {}:{}".format(ex, address, port))
                    if not done:
                        log_me("Client : Write Failed {}:{}".format(address, port))
                        log_me("Client : Waiting for 1 sec after failure {}:{}".format(address, port))
                        #await asyncio.sleep(0.01)
                        break
                    pass

                my_network_state_version = network_state_version

                if done:
                    log_me("Client: CONVERGENCE achieved in client {}:{}".format(address, port))
                    break

                #await asyncio.sleep(0.01)
            if done:
                break

        except Exception as ex:
            log_me("Error = {}".format(ex))
            log_me("Client: Waiting for server {}:{}".format(address, port))
            await asyncio.sleep(0.1)

    log_me('Client : Close socket')
    writer.close()

async def update_async_server(reader, writer):
    global exit_me
    global convergence_achieved
    global network_state
    global waiters

    done = False

    count = 0

    addr = writer.get_extra_info('peername')
    log_me("Server Started for {}".format(addr))

    #obj = netstruct.obj_unpack(b"h$")

    data = b''

    while not exit_me:
        try:

            obj = netstruct.obj_unpack(b"h$")

            while obj.feed(data) != 0:
                data = data + await reader.read(1024)
                log_me("DATA = {}".format(data))

            message = obj.result[0][:]
            data = obj.unused_data[:]

            if len(data) > 0:
                log_me("PARTIAL DATA FOUND {}".format(data))
            else:
                log_me("FULL DATA FOUND {}".format(data))

            message = message.decode()

            if message == '':
                break
            addr = writer.get_extra_info('peername')
            log_me("Server : Received %r from %r" % (message, addr))

            log_me('received "%s"' % message)
            result = False
            if message:
                result = merge_network_state(config_obj, message, network_state)

                if result:
                    while len(waiters) > 0:
                        log_me("Server: Force Clients to send new state..{}.".format(addr))
                        f = waiters.pop(0)
                        f.set_result(True)

            else:
                log_me('No more data from {}'.format(addr))

            if convergence_achieved:
                break

                # print("Server : Send: %r" % message)
                # writer.write(data)
                # await writer.drain()
        except Exception as ex:
            log_me("Server: Client connection failed {} {}".format(addr, ex))
            break

    log_me("Server : Close socket for a client {}".format(addr))
    writer.close()


def check_convergence_achieved(network_state):
    for node in network_state["state"]:
        for my_neighbor in network_state["state"][node]["nodes"]:
            if my_neighbor not in network_state["state"]:
                return False
        if len(network_state["state"][node]["nodes"]) != network_state["state"][node]["num"]:
            return False

    return True


def merge_network_state(config_obj, data, network_state):
    # global mutex
    global convergence_achieved
    global network_state_version

    # mutex.acquire()

    dirty = False

    # try:
    data_json_obj = json.loads(data)
    id = data_json_obj['id']

    # update my node state

    if id not in network_state["state"][config_obj.get_name()]["nodes"]:
        network_state["state"][config_obj.get_name()]["nodes"].append(id)
        dirty = True

    # update other nodes in the network if there is information
    for id in data_json_obj["state"]:
        if id == config_obj.get_name():
            continue

        if id not in network_state["state"]:
            network_state["state"][id] = {}
            network_state["state"][id] = copy.deepcopy(data_json_obj["state"][id])
            dirty = True
            continue

        for j in data_json_obj["state"][id]["nodes"]:
            if j not in network_state["state"][id]["nodes"]:
                network_state["state"][id]["nodes"].append(j)
                dirty = True

    # print (network_state)

    if check_convergence_achieved(network_state):
        log_me("CONVERGENCE ACHIEVED........")
        convergence_achieved = True
    else:
        log_me("CONVERGENCE NOT achieved........")

    if dirty:
        network_state_version += 1
        log_me("Network STATE VERSION {}........".format(network_state_version))

    return dirty



def print_final_network(network_state, output_file, total_time):
    log_me("===================")
    o = open(output_file, "w")
    nodes = list(network_state["state"].keys())
    nodes.sort()

    s = "There are {} machines in this topology. The following are the machines and their neighbors discovered from machine {}:\n".format(len(nodes), network_state['id'])
    o.write(s)
    for node in nodes:
        network_state["state"][node]["nodes"].sort()
        s = "{} : [ {} ] \n".format(node, ", ".join(network_state["state"][node]["nodes"]))
        o.write(s)
        log_me(s)
    s = "Total time taken for discovery for machine {}: {} seconds\n".format(network_state["id"], round(total_time, 2))
    o.write(s)
    log_me(s)
    log_me("===================")
    o.close()


start_time = time.time()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

# register signal handler
signal.signal(signal.SIGINT, exit_gracefully)

config_obj = config.config_read(sys.argv[1])

network_state["id"] = config_obj.get_name()
network_state["state"] = {}
network_state["state"][config_obj.get_name()] = {"nodes": [], "num": len(config_obj.get_neighbors())}

# start query server thread to answer our ID
loop = asyncio.get_event_loop()
coro = asyncio.start_server(update_async_server, config_obj.get_ip(), config_obj.get_port(), loop=loop)
server = loop.run_until_complete(coro)
log_me('Serving on {}'.format(server.sockets[0].getsockname()))

futures = []

for i in config_obj.get_neighbors():
    (addr, port) = i
    log_me(" addr = {}:{}".format(addr, port))
    futures.append(update_async_client(addr, port, loop))

if len(futures) > 0:
    loop.run_until_complete(asyncio.gather(asyncio.wait(futures)))

log_me("WAIT COMPLETED>.....")

if exit_me:
    log_me("Program terminated by User!!")
else:
    log_me("CONVERGENCE ACHIEVED!!!")

if exit_me == False:
    log_me("All clients exited !!")
    total_time = (time.time() - start_time)
    print_final_network(network_state, sys.argv[2], total_time)

logging.info("Program Terminating!!")

sys.exit(0)
