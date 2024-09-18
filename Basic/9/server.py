import socket
HOST = '127.0.0.1'
PORT = 1400
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Đang chờ kết nối...")

ketnoi, diachi= server_socket.accept()

Nhan_dl_tu_client = ketnoi.recv(1024)
print(Nhan_dl_tu_client.decode('utf-8'))

message = input("Nhập tin nhắn gửi đến client: ")
ketnoi.send(message.encode('utf-8'))

ketnoi.close()