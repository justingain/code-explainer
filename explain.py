import sys

def analyze_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)
    functions = [line for line in lines if line.strip().startswith("def ")]

    print("\n📄 Code Analysis\n")
    print(f"Total lines: {num_lines}")
    print(f"Functions found: {len(functions)}")

    if functions:
        print("\nFunctions:")
        for func in functions:
            print(f"- {func.strip()}")

if __name__ == "__main__":
    if len (sys.argv) < 2:
        print("Usage: python explain.py <filename>")
    else:
        analyze_file(sys.argv[1])