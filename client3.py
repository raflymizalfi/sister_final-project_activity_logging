# import socket library because it will use IPC socket
import socket

# Define the destination IP
TCP_IP = '26.51.151.124'

# define the port of the server to connect to
TCP_PORT = 5005

# define buffer size for sending messages
BUFFER_SIZE = 1024

# define the message to be conveyed
first = input("First Name: ")
last = input('Last Name: ')


def email(x, y):
    return '{}{}@gmail.com'.format(x, y).replace(" ", "")


Cemail = email(first, last)

# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connect to the server with the defined IP and Port parameters
s.connect((TCP_IP, TCP_PORT))

# send a message to server
s.send(Cemail.encode())

# receive message from server
data = s.recv(BUFFER_SIZE)

# show message/reply from server
print("Email Created: ", data.decode())
print('Create an Email?')
print('1. Yes')
print('2. No')
print('3. Show Activity Log')
choice = input('Choice?: ')

while 1:
    while choice == '1':
        first = input('First Name: ')
        last = input('Lase Name: ')
        Cemail = email(first, last)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    # Connect to server with the IP parameter and Port that's defined
        s.connect((TCP_IP, TCP_PORT))
    # Send Message to Server
        s.send(Cemail.encode())
    # Receive Message from Server
        data = s.recv(BUFFER_SIZE)
    # Display Messages from Server
        print("Email Created: ", data.decode())
        print('Create an Email?')
        print('1. Yes')
        print('2. No')
        print('3. Show Activity Log')
        choice = input('Choice?: ')
    # Close Connection
    if choice == '2':
        print("Thank you for your attention!")
        s.close()
        break
    if choice == '3':
        f = open('LogRecord.log', 'r')
        file_contents = f.read()
        print(file_contents)
        done = input('Done ? (Y/N) :')
        if done == 'Y' or done == 'y':
            print("Thank you for your attention!")
            f.close
        elif done == 'N' or done == 'n':
            print('Create an Email?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            choice = input('Choice?: ')
    else:
        print("No choices available, select another choice.")
        choice = input('Choice?: ')
    s.close()
    break
