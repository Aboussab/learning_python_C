from ex0 import createur
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.status = ""

    @abstractmethod
    def transform():
        pass

    @abstractmethod
    def revert():
        pass


class Sproutling(createur, HealCapability):
    pass


class Bloomelle(createur, HealCapability):
    pass


class Shiftling(createur, TransformCapability):
    pass


class Morphagon(createur, TransformCapability):
    pass
