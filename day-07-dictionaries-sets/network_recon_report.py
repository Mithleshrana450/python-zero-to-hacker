network = {}

def assign_services(ports):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt"
    }

    result = {}
    for port in ports:
        result[port] = services.get(port, "Unknown")
    return result

def calculate_risk(ports):
    risk = []

    if 22 in ports:
        risk.append("SSH risk")
    if 3306 in ports:
        risk.append("Database exposed")
    if 23 in ports:
        risk.append("Critical (Telnet)")
    if len(ports) > 5:
        risk.append("High risk")

    return risk

def add_host(ip, ports, os):
    network[ip] = {
        "open_ports": ports,
        "services": assign_services(ports),
        "os": os,
        "risk_level": calculate_risk(ports)
    }

def generate_report():
    for ip in network:
        print("\nIP:", ip)
        print("Ports:", network[ip]["open_ports"])
        print("Services:", network[ip]["services"])
        print("OS:", network[ip]["os"])
        print("Risk:", network[ip]["risk_level"])

# Add hosts
add_host("192.168.1.10", [22, 80, 443], "Linux")
add_host("192.168.1.20", [23, 53, 80, 443, 3306, 8080], "Windows")

# Print report
generate_report()