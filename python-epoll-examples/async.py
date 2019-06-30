import logging
import asyncore
import socket
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(created)-15s %(msecs)d %(levelname)8s %(thread)d %(name)s %(message)s")
log = logging.getLogger(__name__)

BACKLOG = 5
SIZE = 1024


class TCPClient(asyncore.dispatcher):
    # time requestor (as defined in RFC 868)

    def __init__(self, host, port=5001):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.is_writable = True
        self.buffer = ""

    def readable(self):
        return True  # We are always happy to read

    def writable(self):
        log.debug("writable called....")
        return self.is_writable # don't have anything to write

    def handle_write(self):
        self.buffer = "Test"

        if self.buffer:
            sent = self.send(self.buffer)
            log.debug("sent data {}".format(sent))
            self.buffer = self.buffer[sent:]
        else:
            log.debug("nothing to send")

        self.is_writable = False

    def handle_connect(self):
        log.debug("Connection successful!!")
        pass # connection succeeded

    def handle_expt(self):
        log.debug("Connection failed...!!")
        self.close() # connection failed, shutdown

    def handle_read(self):
        # get local time
        #here = int(time.time())

        # get and unpack server time
        s = self.recv(SIZE)

        if s:
            log.debug("Received {} {}".format(s, len(s)))
        #there = ord(s[3]) + (ord(s[2])<<8) + (ord(s[1])<<16) + (ord(s[0])<<24L)

        #self.adjust_time(int(here - there))

        #self.handle_close() # we don't expect more data

    def handle_close(self):
        self.close()


class ClientConnectionHandler(asyncore.dispatcher):
    def __init__(self, conn_sock, client_address, server):
        self.server = server
        self.client_address = client_address
        self.buffer = ""

        # We dont have anything to write, to start with
        self.is_writable = False

        # Create ourselves, but with an already provided socket
        asyncore.dispatcher.__init__(self, conn_sock)
        log.debug("created handler; waiting for loop")

    def readable(self):
        return True  # We are always happy to read

    def writable(self):
        return self.is_writable  # But we might not have
        # anything to send all the time

    def handle_read(self):
        log.debug("handle_read")
        data = self.recv(SIZE)
        log.debug("after recv")
        if data:
            log.debug("got data")
            self.buffer += data
            self.is_writable = True  # sth to send back now
        else:
            log.debug("got null data")

    def handle_write(self):
        log.debug("handle_write")
        if self.buffer:
            sent = self.send(self.buffer)
            log.debug("sent data")
            self.buffer = self.buffer[sent:]
        else:
            log.debug("nothing to send")
        if len(self.buffer) == 0:
            self.is_writable = False

    # Will this ever get called?  Does loop() call
    # handle_close() if we called close, to start with?
    def handle_close(self):
        log.debug("handle_close")
        log.info("conn_closed: client_address=%s:%s" % \
                 (self.client_address[0],
                  self.client_address[1]))
        self.close()
        # pass


class Server(asyncore.dispatcher):
    allow_reuse_address = True
    request_queue_size = 5
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM

    def __init__(self, address, handlerClass=ClientConnectionHandler):
        self.address = address
        self.handlerClass = handlerClass

        asyncore.dispatcher.__init__(self)
        self.create_socket(self.address_family,
                           self.socket_type)

        if self.allow_reuse_address:
            self.set_reuse_addr()

        self.server_bind()
        self.server_activate()

    def server_bind(self):
        self.bind(self.address)
        log.debug("bind: address=%s:%s" % (self.address[0], self.address[1]))


    def server_activate(self):
        self.listen(self.request_queue_size)
        log.debug("listen: backlog=%d" % self.request_queue_size)


    def fileno(self):
        return self.socket.fileno()


    def serve_forever(self):
        asyncore.loop()

        # TODO: try to implement handle_request()

        # Internal use


    def handle_accept(self):
        (conn_sock, client_address) = self.accept()
        if self.verify_request(conn_sock, client_address):
            self.process_request(conn_sock, client_address)


    def verify_request(self, conn_sock, client_address):
        return True


    def process_request(self, conn_sock, client_address):
        log.info("conn_made: client_address=%s:%s" % \
                 (client_address[0],
                  client_address[1]))
        self.handlerClass(conn_sock, client_address, self)


    def handle_close(self):
        self.close()

interface = "127.0.0.1"
port = 5001
server = Server((interface, port))

client_1 = TCPClient("127.0.0.1", 5001)
client_2 = TCPClient("127.0.0.1", 5001)

server.serve_forever()

print ("DOne!!!")