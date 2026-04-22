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
