import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communicationSkt, address = server.accept()
    print(f"Connection established with {address}")
    message = communicationSkt.recv(1024).decode('utf-8')
    print(f"{address} send message {message}")
    communicationSkt.send("hello Human !!!".encode('utf-8'))
    communicationSkt.close()
    print(f"connection with {address} ended")