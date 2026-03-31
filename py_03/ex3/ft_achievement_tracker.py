import random


def gen_player_achievements() -> set:
    """
    gen_player_achievements use a large fixed list of achievements to randomly
    assign a set to a player. Choose a random number of achievements
    then pick this number of achievements from the list to build an set

    :return: a set of random acheivment chossen from the list
    :rtype: set
    """
    achievements_list = [
      'Crafting Genius', 'World Savior', 'Master Explorer',
      'Collector Supreme', 'Untouchable', 'Speed Runner',
      'Survivalist', 'Strategist', 'Unstoppable', 'Rotten Explorer',
      'Treasure Hunter', 'First Steps', 'Shiny Collector',
      'Sharp Eyes', 'First Hope', 'Hidden Path Finder'
    ]
    number_acheivment = random.randint(1, len(achievements_list))   
    choosen = random.sample(achievements_list, number_acheivment)
    too_sent = set()
    for ach in choosen:
        too_sent = too_sent.union({ach})
    return too_sent


print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
daylan = gen_player_achievements()

print(f"\nPlayer Alice: {alice}")
print(f"Player Bob: {bob}")
print(f"Player Charlie: {charlie}")
print(f"Player Daylan: {daylan}")

achievements_shared = alice.union(bob, charlie, daylan)
print(f"All distinct achievements: {achievements_shared}")

common = alice.intersection(charlie, bob, daylan)

print(f"Common achievements: {common}")

unique_alice = alice.difference(bob, charlie, daylan)
unique_bob = bob.difference(charlie, alice, daylan)
unique_charlie = charlie.difference(bob, alice, daylan)
unique_daylan = daylan.difference(bob, alice, charlie)

print(f"Only Alice has: {unique_alice}")
print(f"Only Bob has: {unique_bob}")
print(f"Only Charlie has: {unique_charlie}")
print(f"Only Daylan has: {unique_daylan}")

all_achivments = {
      'Crafting Genius', 'World Savior', 'Master Explorer',
      'Collector Supreme', 'Untouchable', 'Speed Runner',
      'Survivalist', 'Strategist', 'Unstoppable', 'Rotten Explorer',
      'Treasure Hunter', 'First Steps', 'Shiny Collector',
      'Sharp Eyes', 'First Hope', 'Hidden Path Finder'}

alice_missing = all_achivments.difference(alice)
bob_missing = all_achivments.difference(bob)
charlie_missing = all_achivments.difference(charlie)
daylan_missing = all_achivments.difference(daylan)

print(f"Alice is missing: {alice_missing}")
print(f"Bob is missing: {bob_missing}")
print(f"Charlie is missing: {charlie_missing}")
print(f"Dylan is missing: {daylan_missing}")
