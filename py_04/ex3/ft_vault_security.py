from typing import Tuple


def secure_archive(fname: str, order: str, content: str | None) -> Tuple[bool , str]:
    flage: bool = False
    sentense: str = ""
    try:
        with open(fname, order) as file:
            if order == "w":
                file.write(content)
                flage = True
                sentense = 'Content successfully written to file'
            elif order == "r":
                sentense = file.read()
                flage = True
    except FileNotFoundError:
        sentense = "[Errno 2] No such file or directory: " + fname
    except PermissionError:
        sentense = "[Errno 13] Permission denied: " +fname
    except Exception as e:
        sentense = e
    return tuple([flage, sentense])

print("=== Cyber Archives Security ===")
print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file", "r", "aloo"))
print()
print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/root/", "r", "aloo"))
print()
print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("ancient_fragment.txt", "r", "aloo"))
print()
print("Using 'secure_archive' to write previous content to a new file:")
print(secure_archive("amine", "w", "aloo"))
