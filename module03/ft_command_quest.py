import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Arguments received: {len(args)}")
    for i in range(len(args)):
        print(f"Argument {i + 1}: {args[i]}")
    
    print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
    main()