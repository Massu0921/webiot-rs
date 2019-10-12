import requests
import json

class WeatherAPI():
    """
    気象情報API処理

    Parameters
    -----------
    jsonpath : str
        appid、位置情報が記述されたjsonのファイルパス
        jsonには以下のよう記述
        {
            "appid" : "Your Client ID",
            "longitude" : "経度",
            "latitude" : "緯度"
        }

    """
    def __init__(self, jsonpath):

        with open(jsonpath, 'r') as cf:
            config = json.load(cf)
        self.appid = config["appid"]
        self.longitude = config["longitude"]
        self.latitude = config["latitude"]

    def get(self):
        """
        天気・降水量取得
        """

        # YOLPリクエストパラメーター
        payload = {
            "appid" : self.appid,   # Client ID
            "output" : 'json',      # 出力方式
            "coordinates" : self.longitude + ',' + self.latitude    # 位置情報(経度, 緯度)
        }

        # リクエスト
        r = requests.get("https://map.yahooapis.jp/weather/V1/place", params=payload)

        # レスポンスをjsonに変換
        data = r.json()

        # 降水量を抽出
        weather_list = data['Feature'][0]['Property']['WeatherList']['Weather']
        precipitation = weather_list[0]['Rainfall']

        return precipitation


if __name__ == '__main__':
    weatherapi = WeatherAPI("config.json")
    print(weatherapi.get())
