from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(target: str) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform():
        pass

    @abstractmethod
    def revert():
        pass
