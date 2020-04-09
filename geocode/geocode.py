import requests
from config.config import api_key


def get_latitude_and_longitude_by_address(address):
    latitude, longitude = None, None
    try:
        url = "https://dapi.kakao.com/v2/local/search/address.json"

        req_url = "{}?query={}".format(url, address);
        r = requests.get(req_url, headers={'Authorization': "KakaoAK {}".format(api_key)})
        data = r.json()

        latitude = data['documents'][0]['y']
        longitude = data['documents'][0]['x']

    except Exception as e:
        print(type(e))
        print(str(e))
    finally:
        return latitude, longitude
