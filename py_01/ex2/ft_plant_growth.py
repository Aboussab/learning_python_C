"""
ft_plant_growth.py - Simulates the growth cycle of plants.

This module defines a Plant class with methods to modify
its state (age and growth)
and tracks these changes over a simulated period of time."""


class Plant:
    """ Represents a plant in the garden that can age and grow.

    Attributes:
        name : The name of the plant.
        height : The current height of the plant in cm.
        days_old : The age of the plant in days"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_cur = age

    def grow(self) -> None:
        """Increases the plant's height by a specific amount."""
        self.height = self.height + 1

    def age(self) -> None:
        """Increments the plant's age by exactly one day."""
        self.age_cur = self.age_cur + 1

    def get_info(self) -> None:
        """Prints the current status of the plant to the console."""
        print(f"{self.name}: {self.height}cm, {self.age_cur} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    borned_highte = rose.height
    for i in range(1, 7):
        rose.age()
        rose.grow()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: + {rose.height - borned_highte}cm")
