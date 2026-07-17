import socket

def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    if s.connect_ex((ip, port)) == 0:
        s.close()
        return True
    else:
        s.close()
        return False


ip = socket.gethostbyname("scanme.nmap.org")
ports = [22, 80, 443, 9999]

for port in ports:
    try:
        service = socket.getservbyport(port)
    except:
        service = "Unknown"

    if is_port_open(ip, port):
        print(port, "-", service, ": Open")
    else:
        print(port, "-", service, ": Closed")