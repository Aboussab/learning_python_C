from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return (count)
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    count = initial_power

    def initial(amount) -> int:
        nonlocal count
        count += amount
        return (count)
    return initial


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner(item_name: str):
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, values: str):
        memory[key] = values

    def recall(key: str) -> str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = spell_accumulator(100)
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 30: {base(30)}")

    print("\nTesting enchantment factory...")
    flaming_outer = enchantment_factory('flaming')
    print(f"{flaming_outer('Sword')}")
    frozen_outer = enchantment_factory('Frozen')
    print(f"{frozen_outer('Shield')}")

    print("\nTesting memory vault...")
    outer = memory_vault()
    stori = outer["store"]
    recalli = outer["recall"]
    stori("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recalli('secret')}")
    print(f"Recall 'unknown': {recalli('unknown')}")


try:
    main()
except Exception:
    print("opps!! somthings went wrong.")
