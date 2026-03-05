"""
Garden Analytics Platform
-------------------------
A system to manage gardens, track plant growth, and calculate statistics
using Object-Oriented Programming patterns (Inheritance, Nested Classes,
Static/Class Methods).
"""


class Plant:
    """
    The base class representing a  plant.
    Tracks name, height, and growth history.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the common attributes for any plant."""
        self.name = name
        self.height = height
        self.age = age
        self.growth_tracker = 0
        self.type = "regular"

    def grow(self, cm) -> None:
        """Increases plant height and updates the growth tracker."""
        self.height = self.height + cm
        self.growth_tracker = cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self) -> str:
        """Returns a string summary of the plant."""
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    A child class representing plants that have flowers.
    Inherits from Plant and adds color and blooming status.
    """
    def __init__(self, name, height, age, colore, bloming):
        """Initializes the common attributes for any floweringplant."""
        super().__init__(name, height, age)
        self.color = colore
        self.bloming = bloming
        self.type = "flowering"

    def get_info(self) -> str:
        """Extend the parent's details string with specific flower info"""
        if self.bloming is True:
            return (super().get_info() + f", {self.color} flowers (blooming)")
        else:
            return (super().get_info() +
                    f",{self.color} flowers (not blooming)")


class PrizeFlower(FloweringPlant):
    """
    A grandchild class representing special flowers.
    Inherits from FloweringPlant and adds prize points.
    """
    def __init__(self, name, height, age, colore, bloming, prize_points):
        """Initializes the common attributes for any prizeflower"""
        super().__init__(name, height, age, colore, bloming)
        self.prize_points = prize_points
        self.type = "prize"

    def get_info(self) -> str:
        """Extend the parent's details string with specific flower info"""
        return (super().get_info() + f", prize_points :{self.prize_points}")


class GardenManager:
    """
    The main controller class. Manages a collection
    of plants for a specific owner.
    Contains nested helper tools for statistics.
    """
    garden_created = 0

    def __init__(self, owner: str) -> None:
        """Initializes the common attributes for any garden object
        attri:
        name = the owner of the garden
        list_plants = list of all  kind of plants they have
        regular,flowering,prize = are a vars that increament every
        time a specifique type has been added """
        self.name = owner
        self.list_plants = []
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        GardenManager.garden_created += 1

    class GardenStats:
        """
        A nested helper class for performing calculations.
        Hidden inside GardenManager to keep logic encapsulated.
        """
        @staticmethod
        def plants_grow(garden) -> None:
            """
            A statice methode that calculate and displays
            statistique for a garden including plants added,
            plant types, and totale adde for growth
            """
            sume = 0
            j = 0
            for x in garden.list_plants:
                sume += x.growth_tracker
                j += 1
            print(f"Plants added: {j}, Total growth: {sume}cm")
            print(f"Plant types: {garden.regular} regular, ", end="")
            print(f"{garden.flowering} flowering,")
            print(f"{garden.prize} prize flowers")

    @classmethod
    def create_garden_network(cls, list_owners: list) -> list:
        """
        method to create multiple GardenManagers at once.
        'cls' refers to the GardenManager class itself.
        """
        garden_list = []
        for x in list_owners:
            garden_list = garden_list + [cls(x)]
        return garden_list

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant object to the garden's list."""
        self.list_plants += [plant]
        if plant.type == "regular":
            self.regular += 1
        elif plant.type == "flowering":
            self.flowering += 1
        elif plant.type == "prize":
            self.prize += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_plants_grow(self, cm):
        """implies "grow()" to every plant in the list."""
        print(f"\n{self.name} is helping all plants grow...")
        for p in self.list_plants:
            p.grow(cm)

    def garden_report(self):
        """Prints a full summary of the garden."""
        print(f"=== {self.name}'s Garden Report ===")
        for x in self.list_plants:
            print(x.get_info())

    def checke_height(self) -> bool:
        """a methode that check all the plants heights to verify that
        are accepted."""
        for x in self.list_plants:
            if x.height < 0:
                return False
        print(f"Height validation test: {True}")
        return True

    @classmethod
    def class_status(cls) -> None:
        """this methode is a clss methode its object is just tell about the
        class status as exemple how many garden we are manageing """
        print(f"Total gardens managed: {cls.garden_created}")


if __name__ == "__main__":
    alice = GardenManager("alice")
    Oak = Plant("Oak tree", 101, 30)
    rose = FloweringPlant("Rose", 25, 16, "red", True)
    Sunflower = PrizeFlower("Sunflower", 25, 16, "red", True, 10)
    print("=== Garden Management System Demo ===")
    print("\n")

    alice.add_plant(Oak)
    alice.add_plant(rose)
    alice.add_plant(Sunflower)
    print("\n\n")

    alice.help_plants_grow(9)
    print("\n")
    alice.garden_report()
    print("\n")

    alice.GardenStats.plants_grow(alice)
    alice.checke_height()
    GardenManager.class_status()
