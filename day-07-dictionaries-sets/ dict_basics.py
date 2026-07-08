target = {
    "ip": "192.168.1.10",
    "port": 22,
    "service": "SSH",
    "os": "Linux",
    "status": "Active"
}

target["vulnerabilities"] = ["Old SSH"]
target["status"] = "Updated"

for key in target:
    print(key, ":", target[key])