import sys

def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__})")
        pandas_ok = True
    except ImportError:
        print("[MISSING] pandas")
        pandas_ok = False

    try:
        import numpy
        print(f"[OK] numpy ({numpy.__version__})")
        numpy_ok = True
    except ImportError:
        print("[MISSING] numpy")
        numpy_ok = False

    if pandas_ok and numpy_ok:
        print("pip vs Poetry:")
        print("Data manipulation ready")
        print("Numerical computation ready")
        print("requirements.txt declares what to install; pip resolves it at install time.")
        print("pyproject.toml declares the same constraints, and Poetry pins the resolved versions in poetry.lock so every install is identical.")
        print("All reagents present and accounted for.")
    else:
        print("\nMissing dependencies detected! Install them using:")
        print("pip install -r ex0/requirements.txt")
        print("OR")
        print("poetry install")

if __name__ == "__main__":
    main()