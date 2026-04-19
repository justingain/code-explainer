# 🧠 Code Explainer CLI

A Python command-line tool that analyzes Python files and provides a structured summary of their contents.

This tool parses source code using Python’s Abstract Syntax Tree (AST) to identify key components such as imports, classes, and functions.

---

## 🚀 Features

- Analyze Python files via CLI
- Count total lines of code
- Detect:
  - Import statements
  - Classes
  - Functions (including methods)
- Generate a human-readable summary of the file structure
- Uses Python AST for accurate code parsing

---

## 🛠 Tech Stack

- Python
- Standard Library (ast, pathlib, sys)

---

## 📦 How to Use

Run the script from the command line:

```bash
python explain.py <filename>
```

Example:
```bash
python explain.py sample.py
```

Example Output:
```
Code Analysis

File: sample.py
Total lines: 15
Imports found: 1
Classes found: 1
Functions found: 3

Imports:
- math

Classes:
- Calculator

Functions:
- square
- add
- multiply

Summary:
This file has 15 lines, 1 import statement(s), 1 class(es), 3 function(s). It appears to use object-oriented structure.
```

## 🧠 How It Works

The tool uses Python’s built-in ast module to parse the source code into a tree structure.

It then walks the tree to identify:

* Import and ImportFrom nodes for dependencies
* ClassDef nodes for classes
* FunctionDef nodes for functions and methods

This approach ensures more accurate analysis compared to simple string matching.

---

## 🔮 Future Improvements

* Add support for nested function analysis
* Detect variables and constants
* Output structured JSON for integration with other tools
* Optional integration with AI-based code explanation

---

## 📄 License

This project is for educational and portfolio purposes.