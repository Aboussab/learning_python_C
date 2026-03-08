class GardenManager:
    plant_list = []

    def __init__(self, name, Water_level, sunlight_hours):
        """Initializes the common attributes for any plant."""
        try:
            if self.name is None:
                raise Exception("Plant name cannot be empty!")
        except Exception as e:
            print(f"Error adding plant: {e}")
        self.name = name
        self.Water_level = Water_level
        self.sunlight_hours = sunlight_hours
        self.plant_list = self.plant_list + [self]
        print(f"Added {self.name} successfully")

    def water_plants(self):
        try:
            print("Opening watering system")
            for x in self.plant_list:
                if (x == "None"):
                    int("abc")
                print(f"Watering {x}")
        except Exception:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    def check_plant_health(self):
        try:
            if self.Water_level > 10:
                raise Exception("Error: Water level 15 is too high (max 10)")
            elif self.Water_level <= 0:
                raise Exception("Error: Water level 15 is too low (min 1)")
            if 2 > self.sunlight_hours:
                raise Exception("Error: Sunlight hours 0 is too low (min 2")
            elif self.sunlight_hours > 12:
                raise Exception("Error: Sunlight hours 0 is too high (max 12")
            print(f"Plant '{self.plant_name}' is healthy!", end="")
            print(f"(water: {self.Water_level}, sun: {self.sunlight_hours})")
        except Exception as e:
            print(e)


def test_garden_management():
    print("Adding plants to garden...")
    p1 = GardenManager("tomato", 5, 8)
    p2 = GardenManager("lettuce", 15, 8)
    p3 = GardenManager(None, 5, 8)
    
    print("Watering plants...")


    print("Checking plant health...")
    p1.check_plant_health()
    p2.check_plant_health()
    