# 선물 db 넣는거 작성하기
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.giftpick

docs = [
        {'tags': ['20', '10', 'female', 'christmas', 'winter', 'small-happy'],
        'info': {'title': 'LUSH 스파권', 'price': '100000',
                 'url': 'https://lush.co.kr/goods/goods_list.php?cateCd=002',
                 'img-url': 'https://media-cdn.tripadvisor.com/media/photo-s/03/3d/40/26/lush-spa.jpg'}},

        {'tags': ['20', '10', 'female', 'christmas', 'winter', 'small-happy'],
        'info': {'title': 'jomalone 크리스마스 코롱 컬렉션', 'price': '142000',
                 'url': 'https://www.jomalone.co.kr/product/25536/80660/christmas2018/rosemagnolia/christmas-cologne-collection',
                 'img-url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRBJjUBZPUadJTF6jGqJvO7OPYpoE4sl7MmNx92In_1zuqdvbFDk_IHsqZBJZGOnp5Wl8-6Pg&usqp=CAc'}},

        {'tags': ['20', '10', 'female', 'christmas', 'winter', 'small-happy'],
        'info': {'title': 'illy 커피 머신', 'price': '130000',
                 'url': 'https://search.shopping.naver.com/catalog/18605518008?cat_id=50002725&frm=NVSCPRO&query=%EC%9D%BC%EB%A6%AC+%EC%BB%A4%ED%94%BC%EB%A8%B8%EC%8B%A0&NaPm=ct%3Dkhn8qyzc%7Cci%3Df64b8f036b5c08f3e17a0e1b36c83e609a57df91%7Ctr%3Dsls%7Csn%3D95694%7Chk%3Dc18192eda6578edb1f389342c37d50401b7effec',
                 'img-url': 'data:image/jpeg;base64,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'}},

        # {'tags': ['10', '0', 'male', 'chri', 'winter', ''],
        # 'info': {'title': '', 'price': '',
        #          'url': '',
        #          'img-url': ''}},
        ]

db.gift.insert_many(docs)
