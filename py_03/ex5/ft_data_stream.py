from typing import Generator
import random


def gen_event() -> Generator[tuple]:
    """
        picks a random name from a list of players, and a random action from
        a list of actions:

        Yields:
            tuple[str, str]: A tuple containing:
                - player name
                - player level
                - event description
    """
    players = ['Alice', 'Bob', 'Charlie', 'Dylan', 'Eve',
               'Frank', 'Grace', 'Hank', 'Ivy', 'Jack']

    actions = ['skate', 'run', 'jump', 'swim', 'dance',
               'sing', 'paint', 'code', 'read', 'sleep']
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(old_list: list) -> Generator:
    while True:
        name = random.choice(old_list)
        old_list.remove(name)
        yield (name)


print("=== Game Data Stream Processor ===")

for x in range(1000):
    kol = next(gen_event())
    print(f"Event {x}: Player {kol[0]} did action {kol[1]}")

list_often = []

for x in range(10):
    list_often.append(next(gen_event()))

print(f"Built list of 10 events: {list_often}")

for x in range(10):
    print(f"Got event from list: {next(consume_event(list_often))}")
    print(f"Remains in list: {list_often}")
