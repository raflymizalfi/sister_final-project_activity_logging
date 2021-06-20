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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

num1 = int(input('Input 1st Number: '))
num2 = int(input('Input 2nd Number: '))
print('Calculation Method:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Modulo')
choice = input('Select Calculation Method: ')



def addition(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def modulo(x, y):
    return x%y

if choice in ('1', '2', '3', '4', '5'):
    if choice == '1':
        result = addition(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choce == '5':
        result = modulo(num1, num2)
else:
    print("Invalid Input or Unavailable Calculation")

# Connect to server with IP and Port parameter
s.connect((TCP_IP, TCP_PORT))

# Send Message to Server
s.send(str(result).encode())

# Receive Message from server
data = s.recv(BUFFER_SIZE)

# Display Message from Server
print("Calculation Complete! Check LogRecord")

# Close Connection
s.close()
