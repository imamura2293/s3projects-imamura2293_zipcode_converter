import requests


def fetch_address(zipcode: str) -> str:
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    response = requests.get(url)

    #郵便番号はすべて、1つの地名に紐づくものとする。
    result  = response.json()['results'][0]

    addess1 = result['address1']
    addess2 = result['address2']
    addess3 = result['address3']

    return f'{addess1}{addess2}{addess3}'


def test_8480046_佐賀県伊万里市伊万里町乙である():
    assert fetch_address(zipcode='8480046') == '佐賀県伊万里市伊万里町乙'
