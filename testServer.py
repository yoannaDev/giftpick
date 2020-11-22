from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.giftpick


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('testHtml.html')


@app.route('/age',methods=)
def age():
    return render_template('select-age.html')


@app.route('/budget?')
def budget():
    return render_template('select-budget.html')


@app.route('/gender')
def gender():
    return render_template('select-gender.html')


@app.route('/mood')
def mood():
    return render_template('select-mood.html')


@app.route('/season')
def season():
    return render_template('select-season.html')


@app.route('/tpo')
def tpo():
    return render_template('select-tpo.html')


@app.route('/result')
def result():
    return render_template('result.html')


## API 역할을 하는 부분
# @app.route('/tag', methods=['POST'])
# def write_tag():
#     # 클라이언트가 준 tags 가져오기
#     tags_receive = request.form.getlist('tags_give[]')
#     title_receive = request.form['title']
#     price_receive = request.form['price']
#     url_receive = request.form['url']
#     db.testgift.insert_one({"title": title_receive, "price": price_receive, "url": url_receive, "tags": tags_receive})
#
#     # 성공 여부 & 성공 메시지 반환
#     return jsonify({'result': 'success', 'msg': '태그 저장 성공'})
#
#
# @app.route('/tag', methods=['GET'])
# def read_candidates():
#     # 1. DB에서 크롤링 정보 모두 가져오기
#     candidates = list(db.test.find({}, {'_id': 0}))
#     # 2. 성공 여부 & 리뷰 목록 반환하기
#     return jsonify({'result': 'success', 'candidates': candidates})
#

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
