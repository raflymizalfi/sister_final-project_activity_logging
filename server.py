# import socket library because it will use IPC socket
import socket
import time
import logging

# define the binding IP address to use
TCP_IP = '26.51.151.124'

# define the port number binding to use
TCP_PORT = 1024

buffer_size = 1024

Format = logging.Formatter("%(levelname)s %(asctime)s - %(message)s")
Handler = logging.FileHandler(filename='LogRecord.log')
Handler.setFormatter(Format)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(Handler)

# create a socket of type TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# do bind to socket
s.bind((TCP_IP, TCP_PORT))
print("socket binded to %s" % (TCP_PORT))

# the server will listen waiting until there is a connection from the client
s.listen(10)
print("socket is listening")

# do loop forever
while 1:
    # accept connection
    conn, addr = s.accept()
    print('Receive data from....')
    print("Address: ", addr)
    data = conn.recv(buffer_size)
    request = data.decode()
    print(request)
    logging.debug(str(request))
    if request == '1':
        f = open('LogRecord.log', 'w')
        f.truncate()
        f.close()
    elif request == '3':
        print("Log Record contents: ")
        f = open('LogRecord.log', 'r')
        file_contents = f.read()
        s.send(file_contents.encode())
        f.close()

    conn . close()
    localtime = time.asctime(time.localtime(time.time()))




