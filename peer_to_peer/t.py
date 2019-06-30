import signal
import time
import sys
import logging
import threading

exit_me = False

main_exit = False

def run_program():
    global exit_me
    global main_exit
    while exit_me == False:
        time.sleep(1)
        print("a")

    main_exit = True
    print ("Bye Bye!!")

def exit_gracefully(signum, frame):
    global exit_me
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    #signal.signal(signal.SIGINT, original_sigint)

    #try:
        #if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
        #   sys.exit(1)
    exit_me = True
    #except KeyboardInterrupt:
    #    print("Ok ok, quitting")
     #   sys.exit(1)

    # restore the exit gracefully handler here
    #signal.signal(signal.SIGINT, exit_gracefully)

#if __name__ == '__main__':
    # store the original SIGINT handler
    #original_sigint = signal.getsignal(signal.SIGINT)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

signal.signal(signal.SIGINT, exit_gracefully)

# start query thread to answer my ID
q = threading.Thread(target=run_program, args=())
q.start()


while (main_exit == False):
    time.sleep(1)
    print ("I am running")

print("I am exitingg")
#run_program()