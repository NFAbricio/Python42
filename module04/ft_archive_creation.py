import sys
import typing

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    
    try:
        f: typing.IO[str] = open(filename, 'r')
        content: str = f.read()
        print(content, end='')
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("Transform data:")
    transformed: str = ""
    
    lines: list[str] = content.split('\n')
    for i in range(len(lines)):
        if i == len(lines) - 1 and lines[i] == "":
            continue
        transformed += lines[i] + "#\n"
        
    print(transformed, end='')

    new_file: str = input("Enter new file name (or empty): ")
    if not new_file:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    try:
        out: typing.IO[str] = open(new_file, 'w')
        out.write(transformed)
        out.close()
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        print(f"Error opening file '{new_file}': {e}")
        print("Data not saved.")

if __name__ == '__main__':
    main()