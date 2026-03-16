import math


def Euclidean_distance(p1: tuple, p2: tuple) -> float:
    """here we have a fct that take 2 3Dpoints and calculate
    the distance between theme using  the 3D Euclidean distance formula
    """
    n = (p2(1) - p1(1)) ** 2 + (p2(2) - p1(2)) ** 2 + (p2(3) - p1(3)) ** 2
    return math.sqrt(n)


def parsing_splited(string: str) -> tuple:
    try:
        list_arg = string.split(",")
        new_tupel = ()
        for x in list_arg:
            new_tupel = new_tupel + (int(x))
    except ValueError:
        print("Error parsing coordinates: invalid literal", end="")
        print(f"for int() with base 10: {x}")


print("=== Game Coordinate System ===")
p1 = (10, 20, 5)
p2 = (0, 0, 0)
print(f"Position created: {p1}")
n = Euclidean_distance(p1, p2)
print(f"Distance between {p1} and {p2}: {n}")
