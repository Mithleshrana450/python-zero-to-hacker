def is_valid_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        num = int(part)
        if num < 0 or num > 255:
            return False

    return True


print(is_valid_ip("192.168.1.1"))      # True
print(is_valid_ip("255.255.255.255"))  # True
print(is_valid_ip("256.100.50.25"))    # False
print(is_valid_ip("192.168.1"))        # False
print(is_valid_ip("192.168.a.1"))      # False