from pathlib import Path
import sys

#!/usr/bin/env python3

def main(swe_path: Path):
    target_string, patterns, expansion_map = read_swe_file(swe_path)
    
    # If target_string is empty, NO
    if not target_string:
        print("NO")
        return

    print(log_expansion_assignments(build_expanded_options(patterns, expansion_map), patterns, target_string))


# How to read a file in Python (https://www.dataquest.io/blog/read-file-python/)
# We read the SWE file line by line, stripping the newline character at the end of each line.
def read_swe_file(file_path) -> tuple[str, list[list[str]], dict[str, list[str]]]:
    with open(file_path, 'r') as swe_file:
        
        try:
            k = int(swe_file.readline().rstrip('\n'))

        except:
            return "", [], {}

        s = swe_file.readline().rstrip('\n')

        patterns = []
        for _ in range(k):
            temp = swe_file.readline().rstrip('\n')
            last_character_was_lowercase = False

            pattern_tokens = []
            for ch in temp:
                if ch.islower():
                    if last_character_was_lowercase:
                        pattern_tokens[-1] += ch

                    else:
                        pattern_tokens.append(ch)
                        last_character_was_lowercase = True
                else:
                    pattern_tokens.append(ch)
                    last_character_was_lowercase = False

            patterns.append(pattern_tokens)

        expansion_map = {}
        for line in swe_file.readlines():
            if ':' not in line:
                continue
            
            letter, values = line.split(':', 1)
            expansion_map[letter] = values.rstrip('\n').split(',')

    return s, patterns, expansion_map

# Build expanded options for each pattern based on the expansion map.
def build_expanded_options(patterns, expansion_map) -> list[list[list[str]]]:
    expanded_options = []

    for pattern in patterns:
        options_for_pattern = []

        for token in pattern:
            # includes lowercase characters as single-option lists
            if isinstance(token, str) and token.islower():
                options_for_pattern.append([token])

            elif token in expansion_map:
                options_for_pattern.append(expansion_map[token])

            else:
                # unknown token -> empty option list
                options_for_pattern.append([])

        expanded_options.append(options_for_pattern)

    return expanded_options

# Backtracking function to find valid expansions
def find_expansions_backtrack(options_list, target_string) -> list[list[str]]:
    """Try to choose one option from each options_list[i] so that the concatenation
    of chosen strings is a substring of target_string. Returns list of successful
    choice-lists (paths)."""
    matches = [] # List to store matches

    if not options_list: # nothing to choose
        return matches

    def backtrack(idx, current, path):
        if idx == len(options_list):
            if current in target_string:
                matches.append(path)
            return
        
        for choice in options_list[idx]:
            if not choice: # skip empty choices
                continue

            new_str = current + choice

            if target_string.find(new_str) == -1: # no match possible
                continue # prune this branch

            backtrack(idx + 1, new_str, path + [choice])

            if matches:
                return # stop at first match

    backtrack(0, "", [])

    return matches

# Log expansion assignments for each pattern
def log_expansion_assignments(options_list, patterns, target_string) -> str:

    log = ''
    for options, pattern in zip(options_list, patterns):
        if not options:
            return "NO" # No options for this pattern

        matches = find_expansions_backtrack(options, target_string)

        if not matches:
            return "NO" # No valid expansions found

        # Print assignments for uppercase letters only
        for match in matches:
            for token, value in zip(pattern, match):
                if isinstance(token, str) and token.isupper():
                    log += f"\n{token}: {value}"

        if patterns.index(pattern) != len(patterns) - 1:
            log += "\n"

    return log



if __name__ == "__main__":
    def swe_file_path(path_str: str) -> Path: # Returns the path
        # Validate and return a .swe file path.
        p = Path(path_str)

        if p.suffix.lower() != ".swe":
            raise ValueError(f"'{path_str}' does not end with .swe") # Raise ValueError if NOT .swe 

        if not p.exists() or not p.is_file():
            raise ValueError(f"File '{path_str}' does not exist or is not a file") # Raise ValueError if FILE does not exist

        return p
    
    args = sys.argv[1:]  # Skips script name

    if len(args) > 1: # Checks for too many input arguments
        print("NO")
        sys.exit()

    try:
        swe_path = swe_file_path(args[0])
        main(swe_path)

    except ValueError as e: # Due to the question constraints, we print NO on any error
        print("NO")
        sys.exit()

    except Exception as e: # Due to the question constraints, we print NO on any error
        print("NO")
        sys.exit()
