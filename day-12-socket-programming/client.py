import socket

client = socket.socket()
client.connect(("localhost", 5000))

message = input("Enter message: ")
client.send(message.encode())

client.close()