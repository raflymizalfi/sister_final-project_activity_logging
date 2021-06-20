# Importing Socket
import socket

# Define IP Address
TCP_IP = '26.51.151.124'

# Define Port
TCP_PORT = 5005

# Define Buffer Size
BUFFER_SIZE = 1024

# Define Message
Message = input("Send a Message: ")

# Create TCP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

# Connect to server with the IP parameter and Port that's defined
s.connect((TCP_IP, TCP_PORT))

# Send message to server
s.send(Message.encode())

# Receive message from server
data = s.recv(BUFFER_SIZE)

# Show Message from Server
print("Message: ", data.decode())

print('Write a Message?')
print('1. Yes')
print('2. No')
print('3. Show Activity Log')
Choice = input('Choice :')

while Choice == '1':
    Message = input("Send a Message : ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
# Connect to server with the IP parameter and Port that's defined
    s.connect((TCP_IP, TCP_PORT))
# Send message to server
    s.send(Message.encode())
# Receive message from server
    data = s.recv(BUFFER_SIZE)
# Display Messages from Server
    print("Message: ", data.decode())
    print('Write a message?')
    print('1. Yes')
    print('2. No')
    print('3. Show Activity Log')
    Choice = input('No: ')
# Close Connection
if Choice == '2':
    print('Thank You')
    s.close()

if Choice == '3':
    f = open('LogRecord.log', 'r')
    file_contents = f.read()
    print(file_contents)
    done = input('Done? (Y/N) :')
    if done == 'Y':
        f.close
s.close()
