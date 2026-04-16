import random

players = [
    'Alice', 'bob', 'Charlie',
    'dylan', 'Emma', 'Gregory',
    'john', 'kevin', 'Liam'
    ]

all_capitalize = [name.capitalize() for name in players]
capitalize_only = [name for name in players if name[0].isupper()]

print(f"Initial list of players: {players}")
print(f"New list with all names capitalized: {all_capitalize}")
print(f"New list of capitalized names only: {capitalize_only}")

score_dict = {name: random.randint(1, 1000) for name in players}
print(f"Score dict: {score_dict}")

average = round(sum(score_dict.values()) / len(score_dict), 2)
print(f"Score average is {average}")

height = {name: score for name, score in score_dict.items() if score > average}
print(f"High scores: {height}")
