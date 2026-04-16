class GardenError(Exception):
    """a simple class that inherits from Exception"""

    pass


class PlantError(GardenError):
    """a simple class that inherits from GardenError"""

    pass


class WaterError(GardenError):
    """a simple class that inherits from GardenError"""

    pass


def valide_age(plant_name, age):
    """
    this is a simple fct that valide if an age is not less then 0
     logic valus if not its rais an error
    """
    if age < 0:
        raise PlantError("Caught PlantError:")
    else:
        print("plant is good")


def valide_liter(plant_name, heurs):
    """this is a simple fct that valide if watring heurs are valide if not it
    rais an error"""
    if heurs < 1:
        raise WaterError("Caught WaterError:")
    else:
        print("all good thanks for ur services!")


def garden_data(name, prix):
    """this is a simple fct that raise an error if an plant prix is more
    than 100dh"""
    if prix > 100:
        raise GardenError("Caught a garden error:")


def test_custom_errors():
    """this is a fct that
    • Shows catching specific custom error types (PlantError, WaterError)
    • Demonstrates inheritance (catching GardenError catches all garden errors)
    """
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        valide_age("Rose", -12)
    except PlantError as e:
        print(f"{e}: there is an mismetch age")

    print("\nTesting WaterError...")
    try:
        valide_liter("Rose", 0)
    except WaterError as e:
        print(f"{e} what a poor plante need more water")

    print("\nTesting catching all garden errors...")
    try:
        valide_age("Rose", -12)
    except GardenError as e:
        print(f"{e}: there is an mismetch age")
    try:
        valide_liter("Rose", 0)
    except GardenError as e:
        print(f"{e}: what a poor plante need more water")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
