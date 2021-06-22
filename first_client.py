# Importing Socket
import socket

# Define IP Address
TCP_IP = '26.51.151.124'

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
Choice = input('Choice: ').strip(" ")

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    s.connect((TCP_IP, TCP_PORT))
    if Choice == '1':
        Message = input("Send a Message: ")
        s.send(Message.encode())
        print("Message:", Message)
        print('Write a message?')
        print('1. Yes')
        print('2. No')
        print('3. Show Activity Log')
        Choice = input('Choice: ').strip(" ")
    elif Choice == '2':
        print(" ")
        print('Thank you for your attention!')
        s.close()
        break
    elif Choice == '3':
        s.send(Choice.encode())
        conn, log_data = s.accept()
        print(log_data)
        print("What will you do now?")
        print("1. Delete Contents")
        print("2. Return")
        nextChoice = input("Choice: ").strip(" ")
        if nextChoice == '1':
            s.send(nextChoice.encode())
            print("Content has been deleted. Check your files.")
            # f = open('LogRecord.log', 'w')
            # f.truncate()
            # print("Content has been deleted. Check your file.")
            # print("1. Delete Contents")
            # print("2. Return")
        elif nextChoice == '2':
            print(" ")
            print('Write a message?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            Choice = input('Choice: ').strip(" ")
        else:
            print('No choices available. Returning to Main.')
            print(" ")
            print('Write a message?')
            print('1. Yes')
            print('2. No')
            print('3. Show Activity Log')
            Choice = input('Choice: ').strip(" ")
    else:
        print("No choices available, select another choice.")
        print(" ")
        print('1. Yes')
        print('2. No')
        print('3. Show Activity Log')
        Choice = input('Choice: ').strip(" ")
s.close()
