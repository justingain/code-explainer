import sys
import ast
from pathlib import Path

def analyze_file(file_path):
    """
    Analyze a Python file and extract structural information such as:
    - number of lines
    - imports
    - classes
    - functions
    """
    path = Path(file_path)

    # Validate that the file exists and is a proper file
    if not path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return
    
    # Read the file contents
    try:
        with open(path, "r", encoding="utf-8") as file:
            source_code = file.read()
    except Exception as error:
        print(f"Error reading file: {error}")
        return
    
    # Parse the file into an Abstract Syntax Tree (AST)
    # This allows us to analyze structure instead of raw text
    try:
        tree = ast.parse(source_code)
    except SyntaxError as error:
        print(f"Syntax error while parsing file: {error}")
        return
    
    lines = source_code.splitlines()
    num_lines = len(lines)

    functions = []
    classes = []
    imports = []

    # Walk through every node in the AST and categorize it
    for node in ast.walk(tree):
        # Detect import statements (e.g., import math)
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        
        # Detect "from x import y" statements
        elif isinstance(node, ast.ImportFrom):
            module_name = node.module if node.module else "unknown"
            imports.append(f"from {module_name}")
        
        # Detect class definitions
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        
        # Detect function definitions (including class methods)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    # Output results
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

    # Add a basic classification of the script type
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