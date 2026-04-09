from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSV():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        phrase: str = ""
        i: int = 0
        print("CSV Output:")
        for x in data:
            phrase += str(x[1])
            i += 1
            if i != len(data):
                phrase += ","
        print(phrase)


class JSON():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        phrase: str = "{"
        i: int = 0
        for x in data:
            phrase += f'"item_{str(x[0])}": "{str(x[1])}"'
            i += 1
            if i != len(data):
                phrase += ","
            else:
                phrase += "}"
        print(phrase)


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
                    self._data_holder.append(x)
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
                print(f"DataStream error - \
Can't process element in stream: {x}")

    def print_processors_stats(self) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
        else:
            for x in self._processors:
                name = type(x).__name__
                extracted = x._rank + len(x._data_holder)
                witing = len(x._data_holder)
                print(f"{name}: total {extracted} \
items processed, remaining {witing} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for x in self._processors:
            big_list = []
            for i in range(nb):
                big_list.append(x.output())
            plugin.process_output(big_list)


print("=== Code Nexus - Data Pipeline ===\n")
print("Initialize Data Stream...\n")
stream = DataStream()
print("== DataStream statistics ==")
print("No processor found, no data")

text_p = TextProcessor()
log_p = LogProcessor()
numeric_p = NumericProcessor()
stream.register_processor(numeric_p)
stream.register_processor(text_p)
stream.register_processor(log_p)
print("Registering Processors")

data = ['Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]
print(f"Send first batch of data on stream: {data}")
stream.process_stream(data)
print("== DataStream statistics ==")
stream.print_processors_stats()
print("Send 3 processed data from each processor to a CSV plugin:")
csv = CSV()
stream.output_pipeline(3, csv)

print("== DataStream statistics ==")
stream.print_processors_stats()

data1: list[any] = [21,
                    ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                    [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                     {'log_level': 'NOTICE', 'log_message':
                      'Certificate expires in 10 days'}],
                    [32, 42, 64, 84, 128, 168], 'World hello']
stream.process_stream(data1)
print("== DataStream statistics ==")
stream.print_processors_stats()
print("Send 5 processed data from each processor to a JSON plugin:")
json = JSON()
stream.output_pipeline(5, json)
print("== DataStream statistics ==")
stream.print_processors_stats()
