import hashlib
import socket
import random
import string

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest(), hashlib.sha256(password.encode()).hexdigest()

def is_valid_ip(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def generate_random_password(length):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for i in range(length))