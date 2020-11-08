from typing import List

from tqdm import tqdm

from fetch_address import fetch_address


def read_zipcodes(input_file: str) -> List[str]:
    with open(input_file, mode='r') as f:
        return f.read().splitlines()


def to_csv(zipcodes: List[str], addresses: List[str], output_file: str) -> None:
    # with open(output_file, mode='w') as f:
    #     for zipcode, address in zip(zipcodes, addresses):
    #         f.write(f'{zipcode},{address}\n')

    optput_lines = []

    for zipcodes, address in zip(zipcodes, addresses):
        output_lines.append(f'{zipcodes},{addresses}')

    output = '\n'.join(output_lines)

    with open(output_file, mode='w') as f:
        f.write(output)


def main():
    zipcodes = read_zipcodes('zipcodes.txt')

    addresses = []

    for zipcode in tqdm(zipcodes):
        address = fetch_address(zipcode)
        addresses.append(address)

        print(address)

    to_csv(zipcodes, addresses, 'output.csv')


if __name__ == '__main__':
    main()
