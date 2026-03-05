"""ft_plant_creation.py - Streamlined creation of Plant objects.

This programe demonstrates how to efficiently initialize multiple
Plant instances using a list of data tuples and a list comprehension,
rather than creating variables manually one by one.
"""


class Plant:
    """
    Represents a plant in the garden with basic biological attributes.

    Attributes:
        name : The common name of the plant.
        height : The current height of the plant in centimeters.
        age : The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name : The name of the plant (e.g., 'Rose').
            height : The starting height in cm.
            age : The starting age in days.
        """
        self.name = name
        self.height = height
        self.age = age


plants = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]]
j = 0
for x in plants:
    plants[j] = Plant(x[0], x[1], x[2])
    j = j + 1
if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for x in plants:
        print(f"Created : {x.name} ({x.height}cm, {x.age} days)")
    print(f"Total plants created: {j}")
