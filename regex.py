import re, requests
from bs4 import BeautifulSoup

# row string
a = 'abcd\n'
#print(a)

b = r'abcd\n'
#print(b)

# re 모듈 search... 
m = re.search(r'abc','123abcdef')
#print(m.start())    # 찾은 패턴 시작 위치
#print(m.end())      # 찾은 패턴 끝 위치 -1
#print(m.group())    # 찾은 패턴 자체를 가져옴
# 패턴 자체가 없을 경우 None 반환

m2 = re.search(r'\d\d','112sdfze45dsfg')    # 처음 찾는 패턴만 

# [] 메타 캐릭터
# [a-zA-Z0-9] -> 모든 알파벳 문자 및 숫자
# [^0-9] -> ^가 맨앞에 오면 not 의미


# 반복 패턴
# '+' -> 1번 이상 패턴 발생
# '*' -> 0번 이상 패턴 발생
# '?' -> 0 또는 1번 패턴 발생
re.search(r'a[bcd]*b','abcbsccb')   # 가장 많은 부분이 매칭된 패턴이 return
re.search(r'b\w+a','banana')
re.search(r'https?','https://www.naver.com')

# ^*, *$
re.search(r'b\w+a','cabana')    # bana 패턴 검색
re.search(r'^b\w+a','cabana')   # ^는 문자열의 맨 앞부터 검색 따라서 매치 안됨
re.search(r'b\w+a$','cabanap')  # $는 문자열의 맨 끝 검색 따라서 매치 안됨

# grouping
m = re.search(r'(\w+)@(.+)','g1063114@gmail.com')   # () 로 그룹을 구분한다
#print(m.group(1))
#print(m.group(2))
#print(m.group(0))

# 다음 뉴스 크롤링 -> 이메일 주소만 찾기

def get_news_content(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text,"html.parser")

    div = page.find('div',attrs={'id':'kakaoContent'})

    content = []
    for i in div.find_all('p',{'dmcf-ptype':'general'}):
        if re.search(r'\w+@.+',i.text) is None:
            pass
        else:
            email = re.search(r'\w+@.+',i.text).group()
            content.append(email)
    
    return content

news = get_news_content('https://news.v.daum.net/v/20210519141045481')
print(news)
    