import os
from datetime import datetime

def log(msg):
    with open("scan.log", "a") as f:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{t} - {msg}\n")

try:
    # 1. Create target list
    targets = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
    with open("targets.txt", "w") as f:
        f.write("\n".join(targets))
    log("targets.txt created")

    # 2. Read targets
    with open("targets.txt", "r") as f:
        targets = f.read().splitlines()
    log("Targets loaded")

    # 3 & 4. Simulated scan and save results
    with open("results.txt", "w") as f:
        for ip in targets:
            result = f"{ip} - Port 80 Open"
            print(result)
            f.write(result + "\n")
            log(f"Scanned {ip}")

    # 7. Summary
    print("\nScan Complete")
    print("Targets Scanned:", len(targets))
    print("Results saved to results.txt")
    print("Logs saved to scan.log")

except FileNotFoundError:
    print("Error: File not found!")
    log("File not found")

except Exception as e:
    print("Error:", e)
    log(str(e))