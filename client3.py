# import socket library because it will use IPC socket
import socket

# Define the destination IP
TCP_IP = '26.51.151.124'

# define the port of the server to connect to
TCP_PORT = 6969

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

# show message/reply from server
print("Email Created:", Cemail)
print('Create an Email?')
print('1. Yes')
print('2. No')
print('3. Show Activity Log')
choice = input('Choice?: ')

while 1:
    if choice == '1':
        first = input('First Name: ')
        last = input('Lase Name: ')
        Cemail = email(first, last)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    # Connect to server with the IP parameter and Port that's defined
        s.connect((TCP_IP, TCP_PORT))
    # Send Message to Server
        s.send(Cemail.encode())
    # Display Messages from Server
        print("Email Created:", Cemail)
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
        print("What will you do now?")
        print("1. Delete Contents")
        print("2. Return")
        nextChoice = input('Choice: ')
        if nextChoice == '1':
            f = open('LogRecord.log', 'w')
            f.truncate()
            print("Contents deleted, check your files.")
            print("1. Delete Contents")
            print("2. Return")
            nextChoice = input('Choice: ')
        if nextChoice == '2':
            f.close()
            print('Create an Email?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            choice = input('Choice?: ')
    else:
        print("No choices available, select another choice.")
        choice = input('Choice?: ')
s.close()
