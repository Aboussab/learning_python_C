from typing import Generator


def data_streams(i: int) -> Generator[list, None, None]:
    """
    Generate a simulated game event.

    Args:
        i (int): Index used to select a player and event cyclically.

    Yields:
        tuple[str, int, str]: A tuple containing:
            - player name
            - player level
            - event description
    """
    gamers = {
        "alice": 5,
        "bob": 12,
        "charlie": 8}

    events = ["killed monster", "found treasure", "leveled up"]

    players_names = list(gamers.keys())
    name = players_names[i % len(players_names)]
    level = gamers[name]
    event = events[i % len(events)]
    yield name, level, event


print("=== Game Data Stream Processor ===")
i = 0
high_level = 0
tr_event = 0
level_up = 0
while i < 3:
    player_name, level, event = next(data_streams(i))
    print(f"Event {i + 1}: Player {player_name} (level {level}) {event}")
    if level > 10:
        high_level += 1
    if event == "found treasure":
        tr_event += 1
    if event == "leveled up":
        level_up += 1
    i += 1

print("...\n=== Stream Analytics ===")
print(f"Total events processed: {i}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {tr_event}")
print(f"Level-up events: {level_up}")
print("\n=== Generator Demonstration ===")
