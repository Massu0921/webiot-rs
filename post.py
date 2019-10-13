import requests
import json
from sensor import *

def post():
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }

    # POSTするデータ
    data = {
        "token": "",            # access token
        "type": "update",       # 処理の種類 (update)
        "ratio": "",            # ホコリの比率[%]
        "concent": "",          # ホコリの濃度[pcs/0.01cf]
        "temp": "",             # 気温[℃]
        "humid": "",            # 湿度[%]
        "press": "",            # 気圧[hPa]
        "light": "",            # 明るさ
        "wind": "",             # 風が強いか(bool)
        "rain": "",             # 雨(センサ, bool)
        "weather": "",          # 現在の天気
        "precipitation": ""     # 降水量(数値)

    }

    # POST
    response = requests.post("POSTするURL", headers=headers, data=json.dumps(data))

if __name__ == "__main__":
    post()
