# Create a tuple for each target:
# pythontargets = [
#     ("192.168.1.1", 80, "HTTP"),
#     ("192.168.1.2", 22, "SSH"),
#     ("192.168.1.3", 443, "HTTPS")
# ]
# Loop through and print each target's details neatly.

pythontargets = [
    ("192.168.1.1", 80, "HTTP"),
    ("192.168.1.2", 22, "SSH"),
    ("192.168.1.3", 443, "HTTPS")
]

for target in pythontargets:
    print(f"IP: {target[0]}, Port: {target[1]}, Service: {target[2]}")