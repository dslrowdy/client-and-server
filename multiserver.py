import socket
from thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
        while True:
                data = c.recv(1024)
                if not data:
                        print_lock.release()
                        break
                print ("Text received for conversion: " + str(data))
                data = str(data).upper()
                print ("Sending converted text: " + str(data))
                c.send(data)
        c.close()

def Main():
        host = '127.0.0.1'
        port = 5000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        s.listen(5)
        while True:
                c, addr = s.accept()
                print_lock.acquire()
                print ("Successful connection from: " + str(addr))
                start_new_thread(threaded, (c,))
        c.close()

if __name__ == "__main__":
        Main()
