import sys

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    
    # Ao importar o módulo dark, a exceção ImportError de dependência circular será levantada.
    from alchemy.grimoire.dark_spellbook import dark_spell_record

if __name__ == "__main__":
    main()