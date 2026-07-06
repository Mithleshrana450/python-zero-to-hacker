# Real wordlist attack structure
def load_wordlist(filename):
    # In real tools this reads from a file
    # We simulate with a list
    wordlist = [
        "admin", "password", "123456",
        "root", "toor", "hacker123",
        "letmein", "qwerty", "abc123"
    ]
    return wordlist

def brute_force(target_user, target_pass, wordlist):
    print(f"[*] Starting brute force on: {target_user}")
    print(f"[*] Wordlist size: {len(wordlist)} passwords")
    print("-" * 40)

    for i, pwd in enumerate(wordlist):
        print(f"[{i+1}/{len(wordlist)}] Trying: {pwd}")
        if pwd == target_pass:
            print(f"\n[+] PASSWORD FOUND: {pwd}")
            print(f"[+] Attempts: {i+1}")
            return pwd

    print("[-] Password not found in wordlist")
    return None

# Run it
words   = load_wordlist("wordlist.txt")
result  = brute_force("admin", "hacker123", words)