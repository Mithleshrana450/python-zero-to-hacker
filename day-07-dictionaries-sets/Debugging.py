student = {
    "name"  : "Mithu",
    "marks" : 95
}

print(student["marks"])

student["marks"] = [95, 88, 92]
total = sum(student["marks"])
print(total)

found_ports = set()
found_ports.add(80)

services = {80: "HTTP", 443: "HTTPS"}
for key, val in services.items():
    print(key, val)