import requests
from bs4 import BeautifulSoup
# URL을 읽어서 HTML를 받아오기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for i in range(1, 20):
    data = requests.get('https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%EC%84%A0%EB%AC%BC&pagingIndex='+ str(i), headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # copy selector로 선물 list 불러오기
    gifts = soup.select('#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div')
    for gift in gifts:
        title = gift.select_one('li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a').text
        if title is not None:
            print(title)
        else:
            print('fail')