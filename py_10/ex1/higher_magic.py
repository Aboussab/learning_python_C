from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combeine(target: str, power: int) -> str:
        return (spell1(target, power), spell2(target, power))
    return combeine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def spell_checker(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return spell_checker


def spell_sequence(spells: list[Callable]) -> Callable:
    def iter_spells(target: str, power: int) -> str:
        return_list = []
        for x in spells:
            return_list.append(x(target, power))
        return return_list
    return iter_spells


def check_condition(target: str, power: int) -> bool:
    if power > 15:
        return True
    else:
        return False


def heal(target: str, power: int) -> str:
    return f"Heal {target} with {power}"


def hits(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def main() -> None:
    print("\nTesting spell combiner...")
    fct = spell_combiner(hits, heal)
    fct_return = fct("Dragon", 15)
    print(f"Combined spell result: {fct_return[0]}, {fct_return[1]}")

    print("\nTesting spell combiner...")
    originale = 10
    multiplied = 3
    power_test = power_amplifier(heal, 3)
    power_test("dragone", 10)
    print(f"Original: {originale}, Amplified: {multiplied * originale}")

    print("\nTesting conditional caster...")
    condition_test = conditional_caster(check_condition, heal)
    print(condition_test("dragone", 15))

    print("\nTesting spell sequence...")
    test_sequence = spell_sequence([heal, hits])
    print(test_sequence("dragon", 150))


try:
    main()
except Exception:
    print("somthing went wrong!!")
