import os

def search_file(start_path, target_file):
    for root, _, files in os.walk(start_path):
        if target_file in files:
            return os.path.join(root, target_file)
    return None

# Start searching from the home directory
start_path = os.path.expanduser("~")  # Expands the "~" to the current user's home directory

target_file = "Homework.pdf"

result = search_file(start_path, target_file)

if result:
    print(f"File found at: {result}")
else:
    print(f"File {target_file} not found.")
