import requests, json

def post():
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }

    # POSTするデータ
    data = {
        "token": "access token",
        "type": "処理の種類 (update)",
        "ratio": "ホコリの比率[%]",
        "concent": "濃度[pcs/0.01cf]",
        "temp": "気温[℃]",
        "humid": "湿度[%]",
        "press": "気圧[hPa]",
        "light": "明るさ",
        "rain": "雨(センサ, bool)",
        "current": "現在雨が降っているか(気象予報API, bool)",
        "forecast": "この後雨が降るか(bool)"
    }

    # POST
    response = requests.post(
        "POSTするURL", headers=headers, data=json.dumps(data))
