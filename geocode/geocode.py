import requests
from config.config import api_key


def get_latitude_and_longitude_by_address(address):
    global latitude, longitude
    try:
        url = "https://dapi.kakao.com/v2/local/search/address.json"

        req_url = "{}?query={}".format(url, address);
        r = requests.get(req_url, headers={'Authorization': "KakaoAK {}".format(api_key)})
        data = r.json()
        if len(data.get('documents', [])) is 0 or data.get('total_count', 0) is 0:
            print('Request: {}, Response: {}'.format(req_url, data))
            return
        latitude = data['documents'][0]['y']
        longitude = data['documents'][0]['x']

    except Exception as e:
        print(type(e))
        print(str(e))
    return latitude, longitude
