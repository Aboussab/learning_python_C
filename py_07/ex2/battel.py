from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act():
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass


class NormalStrategy(BattleStrategy):
    pass


class AggressiveStrategy(BattleStrategy):
    pass


class DefensiveStrategy(BattleStrategy):
    pass
