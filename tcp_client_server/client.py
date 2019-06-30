import socket
import sys
import time

HOST, PORT = "localhost", 8080
retries = 5

do_exit = False

while (True):
    try:
        for i in range(10):
                # Create a socket (SOCK_STREAM means a TCP socket)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to server and send data
                sock.connect((HOST, PORT))

                for j in range(8):

                    data = "REQ\n"
                    sock.sendall(data)

                    # Receive data from the server and shut down
                    received = sock.recv(1024)

                    print "Sent:     {}".format(data.strip())
                    print "Received: {}".format(received.strip())

                    if received.strip() == "END":
                        do_exit = True
                        break


                sock.close()

                if do_exit == True:
                    break

                time.sleep(5)
        break

    except:
        print "connection exception occured \n"
        sock.close()
        time.sleep(5)
        retries -= 1
        continue
