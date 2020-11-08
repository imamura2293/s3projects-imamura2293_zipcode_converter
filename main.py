from tqdm import tqdm

from src.fetch_address import fetch_address
from src.read_zipcodes import read_zipcodes
from src.to_csv import to_csv


def main():
    zipcodes = read_zipcodes('zipcodes.txt')

    addresses = [fetch_address(zipcode) for zipcode in tqdm(zipcodes)]

    to_csv(zipcodes, addresses, 'output.csv')


if __name__ == '__main__':
    main()