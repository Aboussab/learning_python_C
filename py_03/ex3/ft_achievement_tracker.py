alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10',
           'treasure_hunter',
           'boss_slayer',
           'speed_demon',
           'perfectionist'}

print("=== Achievement Tracker System ===")

print(f"\nPlayer alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
achievements_shared = alice.union(bob, charlie)
print(f"All unique achievements: {achievements_shared}")
print(f"Total unique achievements: {len(achievements_shared)}")

print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")

unique_alice = alice.difference(bob, charlie)
unique_bob = bob.difference(charlie, alice)
unique_charlie = charlie.difference(bob, alice)
rare_achievements = unique_alice.union(unique_bob, unique_charlie)
print(f"Rare achievements : {rare_achievements}")

print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
