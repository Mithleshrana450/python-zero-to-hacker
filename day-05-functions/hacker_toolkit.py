def banner():
    # prints a hacker-style banner with your name and tool info
    print("====================================")
    print("         HACKER TOOLKIT")
    print("====================================")

def scan_port(port):
    # checks if port is in open_ports list [22, 80, 443, 3306, 8080]
    # returns "OPEN" or "CLOSED"
    open_ports = [22, 80, 443, 3306, 8080]
    if port in open_ports:
        return "OPEN"
    else:
        return "CLOSED"

def check_password_strength(password):
    # returns "Weak", "Medium", or "Strong"
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

def generate_username(first, last):
    # generates 3 username variations
    # example: mithu_rana, mithu123, m_rana
    username1 = first.lower() + "_" + last.lower()
    username2 = first.lower() + last.lower() + "123"
    username3 = first[0].lower() + "_" + last.lower()
    return username1, username2, username3

    # Main program — call all 4 functions
banner()
print(scan_port(80))
print(check_password_strength("abc123"))
print(generate_username("Mithu", "Rana"))