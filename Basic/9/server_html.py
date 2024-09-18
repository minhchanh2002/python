import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #port = 80, cổng dịch vụ web
cmd = 'GET http://data.pr4e.org HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    print(data.decode()) #giai ma tu byte sang text

mysock.close()