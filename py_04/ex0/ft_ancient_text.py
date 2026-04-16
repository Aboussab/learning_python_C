import sys
import typing
print("=== Cyber Archives Recovery ===")
filename: str | None = None
file: typing.IO | None = None
try:
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    file = open(filename, "r")
    print("---\n")
    content: str = file.read()
    print(content)
    print("\n---")
except IndexError:
    print(f"Usage: {sys.argv[0]} <file>")
except Exception as e:
    print(f"Error opening file '{filename}': {e}")
finally:
    if file is not None:
        file.close()
        print(f"File '{filename}' closed.")
