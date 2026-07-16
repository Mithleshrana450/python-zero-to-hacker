# Polymorphism Example

tools = [
    PortScanner("Nmap", "1.0", "192.168.1.1"),
    WebScanner("Nikto", "2.1", "example.com"),
    PasswordCracker("John", "3.0", "rockyou.txt")
]

for tool in tools:
    print(tool)
    tool.run()