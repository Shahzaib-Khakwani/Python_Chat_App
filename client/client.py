import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello Superior Being".encode('utf-8'))
message = socket.recv(1024).decode('utf-8')
print(message)