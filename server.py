# import socket library because it will use IPC socket
import socket
import time
import logging
import pickle

# define the binding IP address to use
TCP_IP = '26.51.151.124'

# define the port number binding to use
TCP_PORT = 6969

buffer_size = 1024

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='LogRecord.log', level=logging.DEBUG,
                    format=Log_Format)

# create a socket of type TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# do bind to socket
s.bind((TCP_IP, TCP_PORT))
print("socket binded to %s" % (TCP_PORT))

# the server will listen waiting until there is a connection from the client
s.listen(1)
print("socket is listening")

# do loop forever
while 1:
    # accept connection
    conn, addr = s.accept()
    print('Receive data from....')
    print("Address: ", addr)
    data = conn.recv(buffer_size)
    logging.debug(str(data.decode()))
    conn . close()
    localtime = time.asctime(time.localtime(time.time()))


