import json

import requests


def call_api(api_url, headers, params=None):
    try:
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # 에러가 발생하면 예외를 발생시킴
        data = response.json()  # JSON 응답을 파싱하여 Python 데이터로 변환
        return data
    except requests.exceptions.RequestException as e:
        print("API 호출 중 오류 발생:", e)
        return None


with open("yogiyo_info.json", "r", encoding="utf-8") as f:
    headers = json.load(f)["headers"]

# 예제 API URL과 파라미터
# api_url = "https://www.yogiyo.co.kr/api/v1/restaurants-geo/?items=10&order=review_count&page=0&search=&zip_code=471022
api_url = "https://www.yogiyo.co.kr/api/v1/restaurants-geo"
# api_url = "https://www.yogiyo.co.kr/api/v1/restaurants/232424/info/"
# params = {
#     "serving_type": "vd"
# }
# api_url = "https://www.yogiyo.co.kr/api/v1/restaurants/232424/menu/"

# 401 error
# api_url = "https://www.yogiyo.co.kr/api/v1/restaurants"

params = {
    "items": 10,
    "lat": 37.7075366,
    "lng": 127.11693875,
    "order": "owner_reply_count",  # review_count도 가능?
    "page": 0,
    "search": "",
    "serving_type": "vd",
}

# API 호출
result = call_api(api_url, headers, params)

# 결과 확인
if result:
    print("API 호출 성공!")
    print(result)
else:
    print("API 호출 실패.")

print(json.dumps(result, ensure_ascii=False, indent=4))
