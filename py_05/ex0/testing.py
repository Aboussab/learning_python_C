from typing import Any


def validate(data: Any) -> bool:
    if isinstance(data, dict):
        return True
    elif isinstance(data, list) and all(isinstance(x, (dict))for x in data):
        return True
    else:
        return False


def ingest(data: dict | list[dict]) -> None:
    data_holder = []
    if validate(data):
        if isinstance(data, list):
            for x in data:
                for k, v in x.items():
                    data_holder += [str(k), str(v)]
        else:
            for k, v in x.items():
                data_holder += [str(k), str(v)]
    else:
        raise ValueError("Improper text data")
    
    print(data_holder)


# diction = [{"lost": 15}, {"lost": 15}]
# print(validate(diction))
# print(str(diction))
# ingest(diction)
k = "lool"
v = 15
stro = str(f"{str(k)}: {str(v)}")
print(stro)