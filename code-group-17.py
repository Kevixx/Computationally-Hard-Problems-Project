import argparse
from pathlib import Path
import sys

#!/usr/bin/env python3

def main(swe_path: Path):
    k, s, t, R = read_swe_file(swe_path)
    print(k,s,t,R)

# How to read a file in Python (https://www.dataquest.io/blog/read-file-python/)
# We read the SWE file line by line, stripping the newline character at the end of each line.
def read_swe_file(file_path) -> tuple[int, str, list[str], dict[str, list[str]]]:
  swe_file = open(file_path, 'r')

  k = int(swe_file.readline().rstrip('\n'))

  s = swe_file.readline().rstrip('\n')

  t = []
  for i in range(k):
      t.append(swe_file.readline().rstrip('\n'))

  R = {}
  for line in swe_file.readlines():
    letter, values = line.split(':', 1)
    R[letter] = values.rstrip('\n').split(',')

  swe_file.close()
  return k, s, t, R

if __name__ == "__main__":
    # Only accpet .swe files as input
    parser = argparse.ArgumentParser(description="Read a .swe file from the terminal.")
    def swe_file_path(path_str: str) -> Path:
        p = Path(path_str)
        if p.suffix.lower() != ".swe":
            raise argparse.ArgumentTypeError(f"'{path_str}' does not end with .swe")
        if not p.exists() or not p.is_file():
            raise argparse.ArgumentTypeError(f"File '{path_str}' does not exist or is not a file")
        return p
    parser.add_argument("swe_file", type=swe_file_path, help="Path to an input file with .swe extension")

    # Try block to parse arguments and handle errors
    try:
        args = parser.parse_args()
        swe_path: Path = args.swe_file
    except argparse.ArgumentTypeError as e:
        print(f"Argument error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    main(swe_path)
