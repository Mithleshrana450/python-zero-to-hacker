from datetime import datetime

def log(level, message):
    with open("scan.log", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time} [{level}] {message}\n")

# Test logs
log("INFO", "Scan started")
log("INFO", "Port 80 is open")
log("INFO", "Port 443 is open")
log("WARNING", "Port 21 is closed")
log("ERROR", "Connection timeout")
log("INFO", "Host found")
log("WARNING", "Slow response")
log("CRITICAL", "System failure")
log("INFO", "Scan completed")
log("ERROR", "Invalid IP address")

print("10 log entries saved to scan.log")