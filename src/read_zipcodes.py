from typing import List


def read_zipcodes(input_file: str) -> List[str]:
    with open(input_file, mode='r') as f:
        return f.read().splitlines()