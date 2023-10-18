# Bad USB scripts

This script contains sample code to be fetched by a request from a target PC after plugging in a malicious usb that creates a directory named "Maldir" and a file named "new_file.txt" within that directory. Additionally, it provides a template for defining code to be written into the created file.

## Assumptions

1. The target device has Python installed on their system.
2. The target device already has git installed[if not, add command on the malicious USB drive]

### Execution
```bash
python script_name.py
```

## Requirements

- Python (3.x recommended)

## Script Explanation

- The script utilizes the `os` and `subprocess` modules in Python.

- It first checks if a directory named "Maldir" already exists. If not, it creates the directory.

- Then, it defines a file path (`new_file.txt`) within the "Maldir" directory.

- The code to be written into the file can be added after the file path definition.

## Example

```python
# Define the code to be written in the py file
code = """
print("Hello, World!")
"""

# Write the code to the file
with open(file_path, 'w') as file:
    file.write(code)

print(f"Code written to {file_path}.")
```

## Notes

- Make sure to customize the code template according to your requirements.

- The provided example demonstrates how to write a simple "Hello, World!" code to the file.


---

*Note: Replace `script_name.py` with the actual name of your script.*
