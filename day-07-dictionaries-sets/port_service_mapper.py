def get_service(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt",
        27017: "MongoDB"
    }

    return services.get(port, "Unknown")

# Example
print(get_service(80))
print(get_service(22))
print(get_service(9999))