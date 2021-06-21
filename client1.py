# Importing Socket
import socket


# Define IP Address
TCP_IP = '26.220.178.244'

# Define Port
TCP_PORT = 1024

# Define Buffer Size
BUFFER_SIZE = 1024

# Define Sender and Message
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

while True:
    if Choice == '1':
        Message = input("Send a Message: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        s.connect((TCP_IP, TCP_PORT))
        s.send(Message.encode())
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
        print("What will you do now?")
        print("1. Delete Contents")
        print("2. Return")
        nextChoice = input("Choice: ")
        if nextChoice == '1':
            f = open('LogRecord.log', 'w')
            f.truncate()
            print("Content has been deleted. Check your file.")
            print("1. Delete Contents")
            print("2. Return")
            nextChoice = input("Choice: ")
        if nextChoice == '2':
            f.close()
            print('Write a message?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            Choice = input('Choice: ')
        else:
            done = input('No choices available. Would you like to proceed? (Y/N): ')
            if done == 'Y' or done == 'y':
                print('Write a message?')
                print('1. Yes')
                print('2. No')
                print('3. Show Activity Log')
                Choice = input('Choice: ')
            if done == 'N' or done == 'n':
                print("What will you do now?")
                print("1. Delete Contents")
                print("2. Return")
                nextChoice = input('Choice: ')
            else:
                print("No Choices Available")
                print("1. Delete Contents")
                print("2. Return")
                nextChoice = input('Choice: ')
    else:
        print("No choices available, select another choice.")
        print('1. Yes')
        print('2. No')
        print('3. Show Activity Log')
        Choice = input('Choice: ')
s.close()
