import requests
import json

class WeatherAPI():
    """
    気象情報API処理

    Attributes
    -----------
    configjson : str
        appid、位置情報が記述されたjsonのファイルパス
        jsonには以下のよう記述
        {
            "appid" : "Your Client ID",
            "longitude" : "経度",
            "latitude" : "緯度"
        }

    """
    def __init__(self, configjson):

        with open(configjson, 'r') as cf:
            config = json.load(cf)
        self.appid = config["appid"]
        self.longitude = config["longitude"]
        self.latitude = config["latitude"]

    def get(self):
        payload = {
            "appid" : self.appid,
            "output" : 'json',
            "coordinates" : self.longitude + ',' + self.latitude
        }
        r = requests.get("https://map.yahooapis.jp/weather/V1/place", params=payload)
        data = r.json()
        print(data)

if __name__ == '__main__':
    weatherapi = WeatherAPI("config.json")
    weatherapi.get()
