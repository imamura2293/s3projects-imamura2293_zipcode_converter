import requests


def fetch_address(zipcode: str) -> str:
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    response = requests.get(url)

    addess1 = response.json()['results'][0]['address1']
    addess2 = response.json()['results'][0]['address2']
    addess3 = response.json()['results'][0]['address3']

    return response.json()['results']


def test_8480046_佐賀県伊万里市伊万里町乙である():
    assert fetch_address(zipcode='8480046') == '佐賀県伊万里市伊万里町乙'
