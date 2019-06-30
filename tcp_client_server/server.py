import argparse
import asyncore
import socket
import logging

class TaskServer():
    def __init__(self, input_file):
        self.fp = open(input_file)

    def next(self):
        data = None
        try:
            data = self.fp.next()
        except:
            self.fp.close()
        return  data


class AsyncHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(512)
        if data == "REQ\n":
            try:
               send_data = ts.next()
               if send_data != None:
                  self.send(send_data)
               else:
                  self.send("DONE\n")
            except:
               self.send("DONE\n")

class AsyncServer(asyncore.dispatcher):

    def __init__(self, host, port, ts):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.ts = ts

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = AsyncHandler(sock)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help="port", type=int, required=True)
    parser.add_argument('-l', help="listen ip", required=True)
    parser.add_argument('-f', help="task file", required=True)

    cmd_args = parser.parse_args()

    ts = TaskServer(cmd_args.f)

    server = AsyncServer(cmd_args.l, cmd_args.p, ts)
    asyncore.loop()

