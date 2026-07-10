import os
from datetime import datetime

def scan_folder(path):
    try:
        for file in os.listdir(path):
            if file.endswith(".txt") or file.endswith(".py"):
                full_path = os.path.join(path, file)
                size = os.path.getsize(full_path) / 1024
                modified = datetime.fromtimestamp(
                    os.path.getmtime(full_path)
                ).strftime("%Y-%m-%d %H:%M:%S")

                print(f"File: {file}")
                print(f"Size: {size:.2f} KB")
                print(f"Modified: {modified}\n")

    except FileNotFoundError:
        print("Error: Folder not found!")

# Example
scan_folder("C:/Users/YourName/Documents")