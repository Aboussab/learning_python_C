from dark_validator import dark_validate_ingredients  # type: ignore


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arseni", "eyebal"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = dark_validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
