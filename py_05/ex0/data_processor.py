from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._data_holder = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_holder:
            raise IndexError("you cant remov item from empty queue")
        else:
            item = self._data_holder.pop(0)
            current_rank = self._rank
            self._rank += 1
            return tuple([current_rank, item])


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and all(isinstance(x, (int, float))
                                            for x in data):
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                data = [str(x) for x in data]
                for x in data:
                    self._data_holder.append[x]
            else:
                data = str(data)
                self._data_holder.append(data)
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list) and all(isinstance(x, (str))for x in data):
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    self._data_holder = self._data_holder + [x]
            else:
                self._data_holder = self._data_holder + [data]
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list) and all(isinstance(x, (dict)
                                                       )for x in data):
            return True
        else:
            return False

    def ingest(self, data: dict[str: str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    for k, v in x.items():
                        stro = str(f"{str(k)}: {str(v)}")                
                        self._data_holder += [str(stro)]
            else:
                for k, v in data.items():
                    stro = str(f"{str(k)}: {str(v)}")
                    self._data_holder += [stro]
        else:
            raise ValueError("Improper text data")


print("=== Code Nexus - Data Processor ===\n")

print("Testing Numeric Processor...")
test = NumericProcessor()
print(f"Trying to validate input '42': {test.validate(42)}")
print(f"Trying to validate input 'Hello': {test.validate('Hello')}")
try:
    print("Test invalid ingestion of string 'foo' without prior validation:")
    test.ingest('foo')
except ValueError as e:
    print(f"Got exception:{e}")
for x in range(1, 6):
    test.ingest(x)
print("Extracting 3 values...")
for x in range(1, 4):
    tmp = test.output()
    print(f"Numeric value {tmp[0]}: {tmp[1]}")

print()

print("Testing Text Processor...")
text = TextProcessor()
print(f"Trying to validate input '42': {text.validate(42)}")
test_data = ['Hello', 'Nexus', 'World']
for x in test_data:
    text.ingest(x)
print("Extracting 1 value...")
tmp1 = text.output()
print(f"Text value {tmp1[0]}: {tmp1[1]}")

print()

print("Testing Log Processor...")
print("")
log = LogProcessor()
dic = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
       {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
print(f"Processing data: {dic}")
log.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'}])
log.ingest({'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'})
print("Extracting 2 values...")
tmp2 = log.output()
print(f"Log entry {tmp2[0]}: {tmp2[1]}")
tmp2 = log.output()
print(f"Log entry {tmp2[0]}: {tmp2[1]}")
