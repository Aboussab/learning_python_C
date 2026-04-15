from abc import ABC, abstractmethod
import typing


class Creature(ABC):
    def __init__(self):
        self.name: str = ""
        self.c_type: str = ""

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.name} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        pass


class Pyrodon(Creature):
    def attack(self) -> str:
        pass


class Aquabub(Creature):
    def attack(self) -> str:
        pass


class Torragon(Creature):
    def attack(self) -> str:
        pass


class CreatureFactory(ABC):

    @abstractmethod
    def create_base():
        pass

    @abstractmethod
    def create_evolved():
        pass


class FlameFactory(CreatureFactory):
    pass


class AquaFactory(CreatureFactory):
    pass
