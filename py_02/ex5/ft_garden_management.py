class GardenManager:
    plant_list = []

    def __init__(self, name):
        """Initializes the common attributes for any plant."""
        self.name = name

    def add_plants(self, name, Water_level, sun_hours):
        try:
            if not name:
                raise Exception("Plant name cannot be empty!")
            self.plant_list = self.plant_list + [
                [name, Water_level, sun_hours]]
            print(f"Added {name} successfully")
        except Exception as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        try:
            print("Opening watering system")
            for x in self.plant_list:
                if not x[0]:
                    raise Exception("Plant name cannot be empty!")
                print(f"Watering {x[0]}")
        except Exception:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    def check_plant_health(self):
        try:
            for x in self.plant_list:
                if x[2] > 10:
                    raise Exception(
                        "Error: Water level 15 is too hight (max 10)")
                elif x[2] <= 0:
                    raise Exception("Error: Water level 15 is too low (min 1)")
                if 2 > x[1]:
                    raise Exception(
                        "Error: Sunlight hours 0 is too low (min 2")
                elif x[1] > 12:
                    raise Exception(
                        "Error: Sunlight hours 0 is to hight (max 12)")
                print(f"{x[0]}: is healthy!", end="")
                print(f"(water: {x[1]}, sun: {x[2]})")
        except Exception as e:
            print(e)


def test_garden_management():
    print("Adding plants to garden...")
    myFarm = GardenManager("amine")
    myFarm.add_plants("tomato", 6, 12)
    myFarm.add_plants("lettuce", 6, 19)
    myFarm.add_plants("", 6, 12)

    print("\nWatering plants...")
    myFarm.water_plants()
    print("\nChecking plant health...")
    myFarm.check_plant_health()


test_garden_management()
