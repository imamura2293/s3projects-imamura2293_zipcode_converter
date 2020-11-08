from typing import List


def to_csv(zipcodes: List[str], addresses: List[str], output_file: str) -> None:
    output_lines = []

    for zipcode, address in zip(zipcodes, addresses):
        output_lines.append(f'{zipcode},{address}')

    output = '\n'.join(output_lines)

    with open(output_file, mode='w', encoding='utf-8') as f:
        f.write(output)
