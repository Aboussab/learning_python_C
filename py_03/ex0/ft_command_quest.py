import sys

if __name__ == "__main__":
    """
    this is a simple programe where we discover how to read
    argumentsfrom the terminal and use it display it ..,
    """

    print("=== Command Quest ===")
    c = len(sys.argv)
    if c == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if c != 1:
        print(f"Arguments received: {c - 1}")
        i = 0
        for x in sys.argv:
            if i == 0:
                i += 1
                continue
            print(f"Argument {i}: {x}")
            i += 1
    print(f"Total arguments: {c}")
