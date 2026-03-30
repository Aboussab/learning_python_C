import math


def Euclidean_distance(p1: tuple, p2: tuple) -> float:
    """here we have a fct that take 2 3Dpoints and calculate
    the distance between theme using  the 3D Euclidean distance formula
    """
    n = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    return round(math.sqrt(n), 4)


def get_player_pos() -> None:
    """
    get_player_pos is a fct that  Asks the user for the new player
    coordinates in the format x,y,z:
    -Handles improper inputs
    -Retries until a valid set of coordinates is provided
    -Returns a tuple containing the player's current 3D coordinates
    """

    while True:
        phrase = input("Enter new coordinates as floats in format 'x,y,z':")
        cor = phrase.split(",")
        if len(cor) != 3:
            print("Invalid syntax")
            continue
        coords = []
        error = False
        for part in cor:
            try:
                coords.append(float(part))
            except ValueError:
                print(f"Error on Parameter '{part.strip()}\
: could not convert string to float: '{part.strip()}'")
                error = True
                break
        if error:
            continue
        return tuple(coords)


print("\nGet a first set of coordinates")
cord = get_player_pos()
print(f"Got a first tuple:{cord}")
print(f"It includes: X={cord[0]}, Y={cord[1]}, Z={cord[2]}")
Distance = Euclidean_distance((0, 0, 0), cord)
print(f"Distance to center: {Distance}")
print("\nGet a second set of coordinates")
cord2 = get_player_pos()
Distance2 = Euclidean_distance(cord, cord2)
print(f"Distance between the 2 sets of coordinates: {Distance2}")
