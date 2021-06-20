# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
TCP_IP = '26.51.151.124'

# definisikan port dari server yang akan terhubung
TCP_PORT = 5005

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# definisikan pesan yang akan disampaikan
first = input("Nama Depan : ")
last = input('Nama Belakang : ')


def email(x, y):
    return '{}{}@gmail.com'.format(first, last).replace(" ", "")


full = email(first, last)

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((TCP_IP, TCP_PORT))

# kirim pesan ke server
s.send(full.encode())

# terima pesan dari server
data = s.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
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
    pilihan = input('pilihan :')
# tutup koneksi
if pilihan == '2':
    print('Terimakasih sayang')
    s.close()

if pilihan == '3':
    f = open('sample.log', 'r')
    file_contents = f.read()
    print(file_contents)
    done = input('DONE ? (Y/N) :')
    if done == 'Y':
        f.close
s.close()
