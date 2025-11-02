Project: SuperStringWithExpansion — runner (Python)

Purpose
-------
This README explains how to run the Python implementation included in this workspace (script: `code-group-17.py`). The program reads problem instances in the .SWE format, tries to find consistent expansions for uppercase letters so that the expanded patterns become substrings of a given target string, and prints either the chosen expansions or `NO`.

Requirements
-----------
- Python 3.8+ (CPython recommended)
- No external packages required for the provided implementation (pure-Python).

Files
-----
- `code-group-17.py`  — Command-line Python program that reads a `.swe` file and prints either expansion assignments or `NO`.
- `code-group-17.ipynb` — Notebook with analysis, helper code and experimentation.
- `readme-group-17.txt` — (this file) usage and notes.
- `test01.swe` ... `test06.swe` — example SWE input files (if present in the folder).

Input (.SWE) format summary
--------------------------
The program expects a text file structured as follows (ASCII characters only):
1) First line: integer k (number of pattern lines)
2) Second line: target string s (over lowercase alphabet Σ)
3) Next k lines: the strings t_1, t_2, ..., t_k over Σ ∪ Γ (lowercase and uppercase letters)
4) Remaining lines (at most 26; 26 English uppercase letters A–Z): one per uppercase letter in Γ in the form
   LETTER:option1,option2,...
   where each option is a (lowercase) string from Σ. Commas separate expansions.

Example (excerpt):
4
abdde
ABD
DDE
AAB
ABd
A:a,b,c,d,e,f,dd
B:a,b,c,d,e,f,dd
C:a,b,c,d,e,f,dd
D:a,b,c,d,e,f,dd
E:aa,bd,c,d,e

This means k=4, s="abdde", four patterns follow and then expansion lists for uppercase letters.

Program behavior and output
---------------------------
- The program checks whether there exists a choice r_A ∈ R_A, r_B ∈ R_B, ... such that for every pattern t_i the string produced by replacing each uppercase γ by its chosen r_γ (and leaving lowercase letters unchanged) is a contiguous substring of s.
- If no such consistent assignment exists (or input is malformed), the program prints a single line: `NO`.
- If a solution exists, the program prints one assignment per uppercase letter (only letters that appear in the patterns), in the format:
  A:chosen_expansion
  B:chosen_expansion
  ...
  The program prints assignments grouped per pattern (the current implementation prints assignments for each pattern in order).

Command-line usage
------------------
Run from the repository root (or the folder containing `code-group-17.py`) like:

```bash
python3 code-group-17.py path/to/input_file.swe
```

Notes:
- The program enforces that the provided path exists and has the `.swe` extension.
- Output is printed to stdout. Redirect or capture as needed.

Internals / developer notes
---------------------------
The main helper functions in `code-group-17.py` are:
- `read_swe_file(path)` — parses the SWE file and returns (target_string, patterns, expansion_map).
  - `patterns` is a tokenized list: each pattern is a list where lowercase runs are kept as single tokens and uppercase letters are single-character tokens.
- `build_expanded_options(patterns, expansion_map)` — converts a tokenized pattern into a list of option-lists per token; lowercase tokens become single-option lists containing the literal block.
- `find_expansions_backtrack(options_list, target_string)` — backtracking routine that attempts to choose one option from each options_list entry such that the concatenation is a substring of `target_string`. The routine prunes branches where the current prefix cannot appear in `target_string`.
- `log_expansion_assignments(options_list, patterns, target_string)` — orchestrates solving for each pattern and formats output lines.

Testing and debugging tips
--------------------------
- Use small `.swe` files (like `test01.swe`) to validate behavior.
- For performance: pruning is performed via Python's `str.find`. If many substring checks are needed or `s` is large, consider building a suffix automaton or using more advanced incremental matching (KMP state tracking) to speed up checks.
- The code is intentionally simple and readable for assignment purposes; performance improvements (Aho–Corasick, suffix automaton, memoized backtracking) are possible if you need to scale to larger instances.

Examples
--------
Given `test01.swe` in the same folder, run:

```bash
python3 code-group-17.py test01.swe
```

If a solution exists the program prints lines like:
A:a
B:b
...

Otherwise it prints:
NO

Contact
-------
For questions about the implementation you can also look into the notebook `code-group-17.ipynb` for experiments and notes.