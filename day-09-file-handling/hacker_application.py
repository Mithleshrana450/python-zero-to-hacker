import os
from datetime import datetime

def load_wordlist(filepath):
    """Load password wordlist from file"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
        print(f"[+] Loaded {len(passwords)} passwords from {filepath}")
        return passwords
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {filepath}")
        return []
    except PermissionError:
        print(f"[-] Permission denied: {filepath}")
        return []

def save_results(results, output_file):
    """Save scan results to file"""
    try:
        with open(output_file, "w") as f:
            f.write("=" * 50 + "\n")
            f.write("SCAN RESULTS\n")
            f.write(f"Generated: {datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            for result in results:
                f.write(result + "\n")
        print(f"[+] Results saved to {output_file}")
    except PermissionError:
        print(f"[-] Cannot write to {output_file}")

def log_activity(message, level="INFO"):
    """Append to activity log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} [{level}] {message}\n"
    with open("activity.log", "a") as f:
        f.write(log_entry)

# Usage
wordlist = load_wordlist("rockyou.txt")
log_activity("Wordlist loaded successfully")
log_activity("Starting scan on 192.168.1.1", "INFO")