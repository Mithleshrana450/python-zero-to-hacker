class HashResult:
    def __init__(self, password, md5, sha256):
        self.password = password
        self.md5 = md5
        self.sha256 = sha256

    def __str__(self):
        return f"Password: {self.password}, MD5: {self.md5}, SHA256: {self.sha256}"

    def __eq__(self, other):
        return self.md5 == other.md5

    def __len__(self):
        return len(self.password)

    def __contains__(self, char):
        return char in self.password


# Example
h1 = HashResult("admin123", "abc123", "xyz789")
h2 = HashResult("test123", "abc123", "pqr456")

print(h1)
print(h1 == h2)      # True (same MD5)
print(len(h1))       # Password length
print("a" in h1)     # True