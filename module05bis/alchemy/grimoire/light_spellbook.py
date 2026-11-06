def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    # A importação local evita a dependência circular no momento da inicialização do módulo.
    from .light_validator import validate_ingredients
    status = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({status})"