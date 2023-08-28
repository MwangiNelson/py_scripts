import os
import subprocess


# Create a directory
dir_name = "Maldir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} created.")
else:
    print(f"Directory {dir_name} already exists.")

# Create a file in that directory
file_name = "new_file.txt"
file_path = os.path.join(dir_name, file_name)
# Define the code to be written in the py file



