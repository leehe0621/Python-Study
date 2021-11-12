import urllib.request
from bs4 import BeautifulSoup
import warnings # 'https://www.swu.ac.kr'+url 코드 오류 해결 모듈
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
import os

#urlib.request의 urlopen으로 html 리소스 가져오기
web = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue')
#BeuatifulSoup 이용하여 파싱
soup = BeautifulSoup(web, 'html.parser')

#class가 detail인 div 태그의 h2 태그에서 텍스트를 추출하고, 웹툰 제목만 가져오기 위해 strip, split 함수 사용
title = soup.select_one('div.detail>h2').get_text().strip().split('\n')
#회차 정보도 위와 같은 방식으로 추출
episode = soup.find_all("td", {'class':'title'})

os.mkdir(title[0]) #웹툰 제목으로 폴더 생성
os.chdir(title[0]) #웹툰 폴더로 이동

for index, value in enumerate(episode):
    current_episode = value.get_text().strip()
    os.mkdir(current_episode) #폴더 내에 해당 회차의 이름으로 폴더 생성
    os.chdir(current_episode) #해당 폴더로 이동

    #이미지를 저장하기 전 오프너 객체를 생성하여 헤더 추가
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    #이미지 링크 추출
    link = value.find("a")["href"]
    url = ("https://comic.naver.com" + link)
    web2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(web2, 'html.parser')
    img = soup2.find_all("img", {'alt':'comic content'})

    #이미지 저장
    for i, v in enumerate(img):
        path = v["src"]
        urllib.request.urlretrieve(path, str(i) + ".jpg")

    os.chdir('..')