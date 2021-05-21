import requests
from bs4 import BeautifulSoup

url = "https://comment.daum.net/apis/v1/ui/single/main/@20210521174702770"

headers = {
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTYyMTYzOTA4NSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiN2RlMTZiZTktYjA1YS00NjI5LWEzMGUtNjZiMTU4NTlkZmZhIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.E45fHhMuORES2TcYk1rO8KeNZPgBU7wde1Ed1iszp24',
    'Origin':'https://news.v.daum.net',
    'Referer':'https://news.v.daum.net/v/20210521174702770',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

#response = requests.get(url,headers=headers)

#print(response.json()['post']['commentCount']) # 400번대 오류 -> 헤더 추가 -> 정상 동작


#----------------------------------------------------------
# 로그인하기

w_url = "https://stat.wanted.jobs/api/tracking/user"

session = requests.session()

data= {
    'uuid' : 'c881-6cef-f4ef-e682',
    'userid': '1298664',
    'action': 'enter'
}

resp = session.post(w_url,data=data)

print(resp)

my_page = "https://www.wanted.co.kr/profile/likes"

resp = session.get(my_page)
print(resp.text)
content = BeautifulSoup(resp.text,"html.parser")
