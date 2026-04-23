from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    else:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return max(spells)
        elif operation == "min":
            return min(spells)
        else:
            raise ValueError("error! operetore not found.")


def partial_enchanter(base_enchantment: Callable) -> (dict[str, partial[Any]]):
    base_dic = {}
    base_dic["fire"] = partial(base_enchantment, power=50, element="fire")
    base_dic["ice"] = partial(base_enchantment, power=50, element="ice")
    base_dic["lightning"] = partial(
        base_enchantment, power=50, element="lightning"
        )
    return base_dic


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_fct(value: Any):
        return "unknown spell type"

    @base_fct.register(int)
    def _1(value) -> str:
        return f"{value} damage"

    @base_fct.register(str)
    def _2(value) -> str:
        return f"{value}"

    @base_fct.register(list)
    def _3(value) -> str:
        return f"{len(value)} spells"
    return base_fct


def main():
    print("Testing spell reducer...")
    spell_powers = [19, 33, 31, 16, 19, 25]

    spel = spell_reducer(spell_powers, "add")
    print(f"Sum: {spel}")
    spel = spell_reducer(spell_powers, "multiply")
    print(f"Product: {spel}")
    spel = spell_reducer(spell_powers, "max")
    print(f"Max: {spel}")

    print("\nTesting memoized fibonacci...")
    print(f"fib(0): {memoized_fibonacci(0)}")
    print(f"fib(1): {memoized_fibonacci(1)}")
    print(f"fib(10): {memoized_fibonacci(10)}")
    print(f"fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    test_fct = spell_dispatcher()
    print(f"Damage spell: {test_fct(42)}")
    print(f"Enchantment: {test_fct('fireball')}")
    enchantment_types = ['Radiant', 'Frozen', 'Earthen']
    print(f"Damage spell: {test_fct(enchantment_types)}")
    print(f"{test_fct(0.5)}")


try:
    main()
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
