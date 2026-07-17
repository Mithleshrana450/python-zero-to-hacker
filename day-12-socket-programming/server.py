import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Connected by:", addr)

message = conn.recv(1024).decode()
print("Client says:", message)

conn.close()
server.close()