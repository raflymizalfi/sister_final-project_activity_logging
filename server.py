# import library socket karena akan menggunakan IPC socket
import socket
import time
import logging

# definisikan alamat IP binding  yang akan digunakan
TCP_IP = '26.51.151.124'

# definisikan port number binding  yang akan digunakan
TCP_PORT = 5005

buffer_size = 1024

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='LogRecord.log', level=logging.INFO,
                    format=Log_Format)

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((TCP_IP, TCP_PORT))
print("socket binded to %s" % (TCP_PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)
print("socket is listening")

# lakukan loop forever
while 1:
    # menerima koneksi
    conn, addr = s.accept()
    print('Mendapatkan data dari....')
    print("Alamat: ", addr)
    data = conn.recv(buffer_size)
    logging.debug(str(data.decode()))
    conn . close()
    localtime = time.asctime(time.localtime(time.time()))

# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print

# menerima data berdasarkan ukuran buffer

# menampilkan pesan yang diterima oleh server menggunakan print

# mengirim kembali data yang diterima dari client kepada client


# tutup koneksi
