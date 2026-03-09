def garden_operations(err_type):
    if err_type == "bad_data":
        int("abc")
    elif err_type == "divide by zero":
        5 / 0
    elif err_type == "open_file":
        open("missing.txt")
    elif err_type == "key_error":
        dic = {"name": "rose", "age": 2}
        print(dic["height"])


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("bad_data")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("divide by zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("open_file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key_error")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("bad_data")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
