import sys
import typing
print("=== Cyber Archives Recovery ===")
filename: str | None = None
new_file: str | None = None
file: typing.IO | None = None
try:
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    file = open(filename, "r")
    print("---\n")
    content: str = file.read()
    lines: list[str] = content.split("\n")
    print(content)
    content = ""
    for line in lines:
        content = content + line + "#\n"
    print("\n---")
    if file is not None:
        file.close()
        print(f"File '{filename}' closed.")

    print("Transform data:\n---\n")
    print(content)
    print("\n---\n")

    new_file = input("Enter new file name (or empty):")
    if new_file == "":
        x = 5/0
    file2 = open(new_file, "w")
    print(f"Saving data to {new_file}")
    file2.write(content)
    print(f"Data saved in file {new_file}")
    file2.close()
except IndexError:
    print(f"Usage: {sys.argv[0]} <file>")
except ZeroDivisionError:
    print("Not saving data.")
except Exception as e:
    print(f"Error opening file '{filename}': {e}")
