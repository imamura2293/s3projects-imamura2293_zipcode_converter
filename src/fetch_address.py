import requests


def fetch_address(zipcode: str) -> str:
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    response = requests.get(url)
    # 郵便番号はすべて、1つの地名に紐づくものとする。
    result = response.json()['results'][0]

    都道府県名 = result['address1']
    市区町村名 = result['address2']
    町域名 = result['address3']

    return f'{都道府県名}{市区町村名}{町域名}'
