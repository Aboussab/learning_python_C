class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def valide_age(plant_name, age):
    if age < 0:
        raise PlantError("Caught PlantError:")
    else:
        print("plant is good")


def valide_liter(plant_name, heurs):
    if heurs < 1:
        raise WaterError("Caught WaterError:")
    else:
        print("all good thanks for ur services!")


def garden_data(name, prix):
    if prix > 100:
        raise GardenError("Caught a garden error:")


if __name__ == "__main__":
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
