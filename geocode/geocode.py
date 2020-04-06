import requests
from config.config import api_key


def get_latitude_and_longitude_by_address(address):
    global latitude, longitude
    try:
        url = "https://dapi.kakao.com/v2/local/search/address.json"

        r = requests.get("{}?query={}".format(url, address),
            headers={'Authorization': "KakaoAK {}".format(api_key)})
        data = r.json()
        latitude = data['documents'][0]['y']
        longitude = data['documents'][0]['x']

    except Exception as e:
        print(str(e))
    return latitude, longitude
