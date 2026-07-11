import re
import hashlib
import sys
from datetime import datetime

# Real OSINT patterns used in bug bounty recon
PATTERNS = {
    "emails"  : r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "ips"     : r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    "urls"    : r'https?://[^\s<>"{}|\\^`\[\]]+',
    "md5"     : r'\b[a-fA-F0-9]{32}\b',
    "sha256"  : r'\b[a-fA-F0-9]{64}\b',
    "phones"  : r'[6-9]\d{9}'
}

def extract_all(text):
    results = {}
    for name, pattern in PATTERNS.items():
        found = list(set(re.findall(pattern, text)))
        if found:
            results[name] = found
    return results

def hash_target(value):
    """Generate hashes — used in hash cracking prep"""
    return {
        "md5"   : hashlib.md5(value.encode()).hexdigest(),
        "sha1"  : hashlib.sha1(value.encode()).hexdigest(),
        "sha256": hashlib.sha256(value.encode()).hexdigest()
    }

# Command line usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"[*] Hashing: {target}")
        hashes = hash_target(target)
        for algo, h in hashes.items():
            print(f"  {algo.upper():<8}: {h}")
    else:
        print("Usage: python tool.py <password>")