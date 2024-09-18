import socket
HOST = '127.0.0.1'
PORT = 1400

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT)) # Tạo kết nối với Server
message = "Xin chào, máy chủ!"
client_socket.send(message.encode('utf-8')) # Gửi message đến Server
data_from_server = client_socket.recv(1024) # Nhận message từ Server
print(data_from_server.decode('utf-8'))
client_socket.close() #Đóng Socket