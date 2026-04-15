from abc import ABC, abstractmethod
import typing


class Creature(ABC):
    def __init__(self):
        self.name: str = ""
        self.c_type: str = ""

    @abstractmethod
    def attack(self) -> str:
        return f"{self.name}"

    def describe(self) -> str:
        return f"{self.name}"
