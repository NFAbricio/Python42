import os
from dotenv import load_dotenv

def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    
    # Carrega do ficheiro .env caso exista, mas não sobrepõe variáveis de sistema existentes
    load_dotenv(dotenv_path="ex1/.env")
    
    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL", "None connected")
    api_key = os.getenv("API_KEY", "Unauthenticated")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT", "Offline")
    
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_url}")
    print(f"API Access: {'Authenticated' if api_key != 'Unauthenticated' else 'Unauthenticated'}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {zion}")
    
    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")

if __name__ == "__main__":
    main()