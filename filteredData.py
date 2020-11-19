# 선물 db 넣는거 작성하기
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.giftpick

docs = db.test.find()

for doc in docs:
    db.test.update_one({"_id": doc['_id']}, {'$set': {'state': 1}})