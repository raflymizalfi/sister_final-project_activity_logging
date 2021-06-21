# import socket library because it will use IPC socket
import socket

# Define the destination IP
TCP_IP = '26.51.151.124'

# define the port of the server to connect to
TCP_PORT = 5005

# define buffer size for sending messages
BUFFER_SIZE = 1024

# define the message to be conveyed
first = input("First Name : ")
last = input('Last Name : ')


def email(x, y):
    return '{}{}@gmail.com'.format(first, last).replace(" ", "")


full = email(first, last)

# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connect to the server with the defined IP and Port parameters
s.connect((TCP_IP, TCP_PORT))

# send a message to server
s.send(full.encode())

# receive message from server
data = s.recv(BUFFER_SIZE)

# show message/reply from server
print("data diterima : ", data.decode())

print('Ingin kirim pesan lagi ?')
print('1. Ya')
print('2. Tidak')
print('3. Show Activity Log')
pilihan = input('pilihan :')

while pilihan == '1':
    first = input("Nama Depan : ")
    last = input('Nama Belakang : ')
    full = email(first, last)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
    s.connect((TCP_IP, TCP_PORT))
# kirim pesan ke server
    s.send(full.encode())
# terima pesan dari server
    data = s.recv(BUFFER_SIZE)
# tampilkan pesan/reply dari server
    print("data diterima", data.decode())
    print('Ingin generate lagi ?')
    print('1. Ya')
    print('2. Tidak')
    print('3. Show Activity Log')
    pilihan = input('pilihan :')
# tutup koneksi
if pilihan == '2':
    print('Thank You')
    s.close()

if pilihan == '3':
    f = open('LogRecord.log', 'r')
    file_contents = f.read()
    print(file_contents)
    done = input('DONE ? (Y/N) :')
    if done == 'Y':
        f.close
s.close()
