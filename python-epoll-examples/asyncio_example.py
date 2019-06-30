import asyncio
import time
import threading
import sys
import socket

exit_me = False
convergence_achieved = False

async def tcp_echo_client(port, message, loop):
    global exit_me
    global convergence_achieved

    done = False

    while not done and not exit_me:

        try :
            reader, writer = await asyncio.open_connection('127.0.0.1', port,
                                                           loop=loop)
            print("My ID tcp_echo_client = ", threading.get_ident())

            while not exit_me:

                if convergence_achived:
                    done = True

                print('Client: Send: %r' % message)
                try:
                    writer.write(message.encode())
                    await writer.drain()
                except Exception as ex:
                    print ("Write Failed....")

                    print("Waiting for 1 sec after failure....")
                    await asyncio.sleep(1)
                    break
                if done:
                    print("convergence achieved in client....")
                    await asyncio.sleep(1)
                    break

                #data = await reader.read(100)
                #print('Client : Received: %r' % data.decode())
                print("Waiting for 1 sec with success...")
                await asyncio.sleep(1)
        except:
            print ("Waiting for server......")
            await asyncio.sleep(1)



    print('Client : Close socket')
    writer.close()

async def handle_echo(reader, writer):
    global exit_me
    global convergence_achieved
    print("My ID handle_echo = ", threading.get_ident())

    done = False

    count = 0

    while not exit_me:
        try:
            data = await reader.read(100)
            if data is None or data == '':
                print ("data = ", data)
                break
            message = data.decode()

            if message == '':
                print("message = ", message)
                break
            addr = writer.get_extra_info('peername')
            print("Server : Received %r from %r" % (message, addr))

            count += 1

            if count > 5:
                convergence_achived = True
                break

            #print("Server : Send: %r" % message)
            #writer.write(data)
            #await writer.drain()
        except:
            print ("Server: Client connection failed....")
            break


    #exit_me = True
    #await asyncio.sleep(5)
    print("Server : Close socket....")
    writer.close()

print ("My ID = ", threading.get_ident())
loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', int(sys.argv[1]), loop=loop)
server = loop.run_until_complete(coro)

message = 'Hello World!'

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))

#f1 = asyncio.ensure_future(tcp_echo_client(message, loop))
#f2 = asyncio.ensure_future(tcp_echo_client(message, loop))
#f3 = asyncio.ensure_future(tcp_echo_client(message, loop))

other_port = int(sys.argv[2])
f1 = tcp_echo_client(other_port, message, loop)
f2 = tcp_echo_client(other_port, message, loop)
f3 = tcp_echo_client(other_port, message, loop)

f = [ f1, f2, f3 ]

loop.run_until_complete(asyncio.gather(asyncio.wait(f)))
#try:
#    loop.run_forever()
#except KeyboardInterrupt:
#    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()