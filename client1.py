# Importing Socket
import socket
import copy

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

# Show Message from Server
print("Message:", Message)
print('Write a Message?')
print('1. Yes')
print('2. No')
print('3. Show Activity Log')
Choice = input('Choice: ')

while 1:
    while Choice == '1':
        Message = input("Send a Message: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    # Connect to server with the IP parameter and Port that's defined
        s.connect((TCP_IP, TCP_PORT))
    # Send message to server
        s.send(Message.encode())
    # Receive message from server
        data = s.recv(BUFFER_SIZE)
    # Display Messages from Server
        print("Message:", Message)
        print('Write a message?')
        print('1. Yes')
        print('2. No')
        print('3. Show Activity Log')
        Choice = input('Choice: ')
    # Close Connection
    if Choice == '2':
        print('Thank you for your attention!')
        s.close()
        break
    if Choice == '3':
        f = open('LogRecord.log', 'r')
        file_contents = f.read()
        print(file_contents)
        print("1. Delete Contents")
        print("2. Copy File")
        print("3. Return")
        print("What will you do now?")
        nextChoice = input("Choice: ")
        if nextChoice == '1':
            f.truncate()
            print("Content has been deleted. Check your file.")
        if nextChoice == '2':
            copy.deepcopy(f)
            print("Content has been copied. Check your folder")
        if nextChoice == '3':
            print('Write a message?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            Choice = input('Choice: ')
        else:
            done = input('Done? (Y/N) :')
            if done == 'Y' or done == 'y':
                f.close()
                print('Write a message?')
                print('1. Yes')
                print('2. No')
                print('3. Show Activity Log')
                Choice = input('Choice: ')
            if done == 'N' or done == 'n':
                nextChoice = input("What will you do now?")
                print("1. Delete Contents")
                print("2. Copy File")
                print("3. Return")
    else:
        print("No choices available, select another choice.")
        Choice = input('Choice: ')
    s.close()
    break
