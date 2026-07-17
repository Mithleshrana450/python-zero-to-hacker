import socket

s = socket.socket(socket.AF_INET)

s.connect(("192.168.1.1", 80))

s.settimeout(5)

data = s.recv(1024)

result = s.connect_ex(("192.168.1.1", 80))