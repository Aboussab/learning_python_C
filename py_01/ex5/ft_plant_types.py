class Plant:
    """
    A base class representing a plant in the garden.

    Attributes:
        name : The common name of the plant.
        height : The height of the plant in cm.
        age : The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the common attributes for any plant."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    A specialized class for Flowers, inheriting from Plant.
    Adds specific attributes for color and blooming behavior.
    """
    def __init__(self, name: str, height: int, age: int, colore: str) -> None:
        """
        Initializes a Flower instance.
        Args:
            color : The color of the flower petals.
        """
        super().__init__(name, height, age)
        self.color = colore

    def bloom(self):
        """Simulates the flower blooming by printing a message."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """Prints the specific details of the flower including its color."""
        print(f"{self.name}: {self.height}cm, {self.age} days, ", end="")
        print(f"{self.color} color")


class Tree(Plant):
    """
    A specialized class for Trees, inheriting from Plant.
    Adds specific attributes for trunk size and shade calculation.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """
        Initializes a Tree instance.
        Args:
            trunk_diameter : The diameter of the tree trunk in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculates and prints the shade area based on trunk diameter.
        Formula: trunk_diameter/2 * 3.14
        (took it from the example in the subject)
        """
        n = (self.trunk_diameter/2) * 3.14
        print(f"{self.name} provides {n} square meters of shade")

    def get_info(self) -> None:
        """Prints the specific details of the tree including trunk diameter."""
        print(f"{self.name}: {self.height}cm, {self.age} days,", end="")
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    A specialized class for Vegetables, inheriting from Plant.
    Adds specific attributes for harvest season and nutrition.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initializes a Vegetable instance.
        Args:
            harvest_season : The time of year best for harvesting.
            nutritional_value : Key vitamin or nutrient information.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Prints the specific details of the vegetable
        including harvest season, and the nutritional value of the vegetable.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days, ", end="")
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


rose = Flower("Rose", 25, 15, "red")
rose.get_info()
rose.bloom()

print("\n")
oke = Tree("Oak", 500, 1825, 50)
oke.get_info()
oke.produce_shade()
print("\n")
tomate = Vegetable("Tomato", 80, 90, "summer", "vitamine C")
tomate.get_info()
