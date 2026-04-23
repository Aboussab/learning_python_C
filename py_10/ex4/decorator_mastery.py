from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*arg, **kwargs):
        print(f"Casting {func.__name__} ....")
        start = time.time()
        fct = func(*arg, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return fct
    return wrapper


def power_validator(min_power: int) -> Callable:
    def factory_dic(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            return ("Insufficient power for this spell")
        return wrapper
    return factory_dic


def retry_spell(max_attempts: int) -> Callable:
    def factory_dic(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    succsed = func(*args, **kwargs)
                    return succsed
                except Exception:
                    print(f"Spell failed, \
retrying... (attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return factory_dic


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def Fireball(target: str, power: int) -> str:
    return "Fireball cast!"


@retry_spell(3)
def always_fails(target: str, power: int) -> str:
    raise Exception("Always fails!")


def main():
    print("Testing spell timer...")
    print(f"Result: {Fireball("firball", 155)}")

    print("\nTesting retrying spell...")
    print(always_fails("Dragon", 50))

    print("\nTesting MageGuild...")
    tmp_obje = MageGuild()
    print(tmp_obje.validate_mage_name("amine"))
    print(tmp_obje.validate_mage_name("4651"))
    print(tmp_obje.cast_spell("Lightning", 15))
    print(tmp_obje.cast_spell("Lightning", 8))


try:
    main()
except Exception:
    print("Oopps!! somthings went wrong.")
