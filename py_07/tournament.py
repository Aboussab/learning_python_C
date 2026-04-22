from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures_and_strategies = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    for i in range(len(creatures_and_strategies)):
        for j in range(i + 1, len(creatures_and_strategies)):
            creature1, strategy1 = creatures_and_strategies[i]
            creature2, strategy2 = creatures_and_strategies[j]

            print()
            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    opponents0 = [
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(opponents0)

    print()
    print("Tournament 1 (error)")
    opponents1 = [
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ]
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(opponents1)

    print()
    print("Tournament 2 (multiple)")
    opponents2 = [
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ]
    print(" [ (Aquabub+Normal), (Healing+Defensive),\
 (Transform+Aggressive) ]")
    battle(opponents2)
