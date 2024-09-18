import socket

def start_server():
    # Tạo một socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('Server đang lắng nghe trên địa chỉ:', server_socket.getsockname())

    while True:
        # Chấp nhận kết nối từ client
        client_socket, client_address = server_socket.accept()
        print('Kết nối từ:', client_address)

        # Nhận tệp tin từ client
        with open('received_file.txt', 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)

        print('Đã nhận tệp tin từ client, nội dung tệp tin:')
        with open('received_file.txt', 'r') as f:
            print(f.read())

        client_socket.close()

if __name__ == "__main__":
    start_server()
