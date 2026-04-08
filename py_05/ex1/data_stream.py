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


class DataStream():
    def __init__(self):
        self._processors: list[DataProcessor] = []
    
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
    
    def process_stream(self, stream: list[Any]) -> None:
        for x in stream:
            flaf: bool = False
            for y in self._processors:
                if y.validate(x):
                    y.ingest(x)
                    flaf = True
                    break
            if not flaf:
                print(f"DataStream error - Can't process element in stream: {x}")
    
    def print_processors_stats(self) -> None:
        for x in self._processors:
            name = type(x).__name__
            extracted = x._rank
            witing = len(x._data_holder)
            print(f"{name}: total {extracted} items processed, remaining {witing} on processor")


stream = DataStream()
data = ['Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
         42, ['Hi', 'five']
         ]
text_p = TextProcessor()
numeric_p = NumericProcessor()
log_p = LogProcessor()


stream.register_processor(numeric_p)

stream.process_stream(data)

stream.register_processor(text_p)
stream.register_processor(log_p)

