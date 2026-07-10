# Create file with 5 IPs
ips = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "172.16.0.1", "8.8.8.8"]

with open("targets.txt", "w") as f:
    f.write("\n".join(ips))

# Read and print IPs
with open("targets.txt", "r") as f:
    print(f.read())

# Add 2 more IPs
with open("targets.txt", "a") as f:
    f.write("\n1.1.1.1\n192.168.1.1")

# Count targets
with open("targets.txt", "r") as f:
    ips = f.read().splitlines()
print("Total targets:", len(ips))

# Remove duplicates
ips = list(dict.fromkeys(ips))
with open("targets.txt", "w") as f:
    f.write("\n".join(ips))

print("Unique targets:", len(ips))