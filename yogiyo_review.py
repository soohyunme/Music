import requests


def call_api(api_url, params=None):
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # 에러가 발생하면 예외를 발생시킴
        data = response.json()  # JSON 응답을 파싱하여 Python 데이터로 변환
        return data
    except requests.exceptions.RequestException as e:
        print("API 호출 중 오류 발생:", e)
        return None


# 예제 API URL과 파라미터
api_url = "https://www.yogiyo.co.kr/api/v1/reviews/462893/"
params = {"count": 50, "only_photo_review": True, "page": 1, "sort": "time"}


result = call_api(api_url, params)

# 결과 확인
if result:
    print("API 호출 성공!")
    print(result)
else:
    print("API 호출 실패.")
