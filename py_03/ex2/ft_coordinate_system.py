import math


def Euclidean_distance(p1: tuple, p2: tuple) -> float:
    """here we have a fct that take 2 3Dpoints and calculate
    the distance between theme using  the 3D Euclidean distance formula
    """
    n = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    return math.sqrt(n)


def parsing_splited(string: str) -> tuple | None:
    """
    here we have a fct that parsed an argument and split it by ',' and convert
    it into a tupel of int:

    :param string: fom the areg we take the string to work on it
    :type string: str
    :return: it return an tuple if parsing and split goes well if not return
    None and catch an error
    :rtype: tuple | None
    """
    try:
        list_arg = string.split(",")
        new_tupel = ()
        for x in list_arg:
            new_tupel = new_tupel + (int(x),)
        return new_tupel
    except ValueError:
        print("Error parsing coordinates: invalid literal", end="")
        print(f"for int() with base 10: {x}")
        return None


print("=== Game Coordinate System ===")
p1 = (10, 20, 5)
p2 = (0, 0, 0)
print(f"Position created: {p1}")
n = Euclidean_distance(p1, p2)
print(f"Distance between {p1} and {p2}: {n:.2f}")

phrase = "3,4,0"
print(f"\nParsing coordinates: \"{phrase}\"")
p3 = parsing_splited(phrase)
if p3 is not None:
    print(f"Position created: {p3}")
    n = Euclidean_distance(p3, p2)
    print(f"Distance between {p3} and {p2}: {n}")
else:
    print("Error details - Type: ValueError, Args: (\"invalid literal for"
          + "int() with base 10:\")"
          )

phrase = "abc,def,ghi"
print(f"\nParsing coordinates: \"{phrase}\"")
p4 = parsing_splited(phrase)
if p4 is not None:
    print(f"Position created: {p4}")
    n = Euclidean_distance(p4, p2)
    print(f"Distance between {p4} and {p2}: {n}")
else:
    print("Error details - Type: ValueError, Args: (\"invalid literal for "
          + f"int() with base 10:\"{phrase}\")")

print("\nUnpacking demonstration:")
p5 = (3, 4, 0)
x, y, z = p5
print(f"Player at x={x}, y={y},z={z}")
print(f"Coordinates: X={x}, Y={y},  Z={z}")
