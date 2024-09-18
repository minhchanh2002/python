import socket

def send_file(filename):
    # Tạo một socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Gửi tệp tin đến server
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)

    client_socket.close()

if __name__ == "__main__":
    send_file('Hello.txt')