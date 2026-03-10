class GardenError(Exception):
    """a simple class that inherits from Exception"""

    pass


class PlantError(GardenError):
    """a simple class that inherits from GardenError"""

    pass


class WaterError(GardenError):
    """a simple class that inherits from GardenError"""

    pass


class GardenManager:
    """this  is an simple class that mange an garden with its diffrents
    methode
    """

    plant_list = []

    def __init__(self, name):
        """Initializes the common attributes for any plant."""
        self.name = name

    def add_plants(self, name, Water_level, sun_hours):
        """method validates input and raises errors appropriately"""
        try:
            if not name:
                raise GardenError("Plant name cannot be empty!")
            list_ts = [name, Water_level, sun_hours]
            self.plant_list = self.plant_list + [list_ts]
            print(f"Added {name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        """here we have a fct that  clean up after itself,
        even if an error happens its open the watrings syst
        and waters each plant if an error happned its close the systeme"""
        try:
            print("Opening watering system")
            for x in self.plant_list:
                if not x[0]:
                    raise GardenError("Plant name cannot be empty!")
                print(f"Watering {x[0]}")
        except GardenError:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    def check_plant_health(self):
        """this is a fct that :
        Validates plant name (not empty)
        • Validates water level (1-10 range)
        • Validates sunlight hours (2-12 range)
        • Raises ValueError with descriptive messages for invalid inputs
        • Returns success message for valid inputs
        """
        try:
            for x in self.plant_list:
                if x[1] > 10:
                    msg = "Error in " + x[0] + ": Water level 15 is too hight"
                    raise WaterError(msg)
                elif x[1] <= 0:
                    msg = "Error in " + x[0] + "level 15 is too low (min 1)"
                    raise WaterError(msg)
                if 2 > x[2]:
                    msg = "Error in " + x[0] + ": Sunlight hours is too low "
                    raise PlantError(msg)
                elif x[2] > 12:
                    msg = "Error in " + x[0] + ": Sunlight hours is to hight"
                    raise PlantError(msg)
                print(f"{x[0]}: is healthy!", end="")
                print(f"(water: {x[1]}, sun: {x[2]})")
        except WaterError as e:
            print(e)
        except PlantError as e:
            print(e)


def test_garden_management():
    """this a fct that :
    • Tests adding plants (good and bad inputs)
    • Tests watering system with cleanup
    • Tests plant health checking
    • Shows error recovery mechanisms
    """
    print("Adding plants to garden...")
    myFarm = GardenManager("amine")
    myFarm.add_plants("tomato", 6, 12)
    myFarm.add_plants("lettuce", 6, 19)
    myFarm.add_plants("", 6, 12)

    print("\nWatering plants...")
    myFarm.water_plants()
    print("\nChecking plant health...")
    myFarm.check_plant_health()


print("=== Garden Management System ===")
test_garden_management()
