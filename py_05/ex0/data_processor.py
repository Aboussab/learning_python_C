from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, bool)):
            return False
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and all(isinstance(x, (int, float))
                                            for x in data):
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                data = [str(x) for x in data]
            else:
                data = str(data)
        else:
            raise ValueError(f"Test invalid ingestion of string '{data}'\
without prior validation")


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass
