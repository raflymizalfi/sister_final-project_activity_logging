# Import socket and logging
import socket
import logging

# Define IP
TCP_IP = '26.51.151.124'

# Define Port
TCP_PORT = 5005

# Define Buffer Size
BUFFER_SIZE = 1024

# Create socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

num_1 = 10
num_2 = 2


def add(x, y):
    print('Addition', x, y)
    return x+y


add_result = add(num_1, num_2)

# Connect to server with IP and Port parameter
s.connect((TCP_IP, TCP_PORT))

# Send Message To server
s.send(str(add_result).encode())
# Receive Message from server
data = s.recv(BUFFER_SIZE)

# Display Message from Server

# Display Message from Server
print("Data Recieved!")

# Close Connection
s.close()
