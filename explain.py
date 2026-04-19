import sys
from pathlib import Path

def analyze_file(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as error:
        print(f"Error reading file: {error}")
        return
    
    num_lines = len(lines)

    functions = []
    classes = []
    imports = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("def "):
            functions.append(stripped)
        elif stripped.startswith("class "):
            classes.append(stripped)
        elif stripped.startswith("import ") or stripped.startswith("from "):
            imports.append(stripped)

    print("\n Code Analysis\n")
    print(f"File: {path.name}")
    print(f"Total lines: {num_lines}")
    print(f"Imports found: {len(imports)}")
    print(f"Classes found: {len(classes)}")
    print(f"Functions found: {len(functions)}")

    if imports:
        print("\nImports:")
        for item in imports:
            print(f"- {item}")
    
    if classes:
        print("\nClasses:")
        for item in classes:
            print(f"- {item}")
    
    if functions:
        print("\nFunctions:")
        for item in functions:
            print(f"- {item}")
    
    print("\nSummary:")
    print(build_summary(num_lines, imports, classes, functions))

def build_summary(num_lines, imports, classes, functions):
    parts = [f"This file has {num_lines} lines"]

    if imports:
        parts.append(f"{len(imports)} import statement(s)")

    if classes:
        parts.append(f"{len(classes)} class(es)")
    
    if functions:
        parts.append(f"{len(functions)} function(s)")

    summary = ", ".join(parts) + "."

    if functions and not classes:
        summary += " It appears to be a function-based script"
    elif classes:
        summary += " It appears to use object-oriented structure"
    else:
        summary += " It appears to be a simple script"

    return summary

if __name__ == "__main__":
    if len (sys.argv) < 2:
        print("Usage: python explain.py <filename>")
    else:
        analyze_file(sys.argv[1])