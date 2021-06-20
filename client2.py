# import library socket karena akan menggunakan IPC socket
import socket
import logging

# definisikan tujuan IP server
TCP_IP = '127.0.0.1'

# definisikan port dari server yang akan terhubung
TCP_PORT = 5005

buffer_size = 1024


# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

num_1 = 10
num_2 = 2


def add(x, y):
    print('Penjumlahan', x, y)
    return x+y


add_result = add(num_1, num_2)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((TCP_IP, TCP_PORT))

# kirim pesan ke server
s.send(str(add_result).encode())
# terima pesan dari server


# tampilkan pesan/reply dari server

# tampilkan pesan/reply dari server
print("Data diterima")

# tutup koneksi
s.close()
