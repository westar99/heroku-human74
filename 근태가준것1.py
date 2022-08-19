# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import sys
import json
import random
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
		# Heroku
    engine = create_engine("postgresql://uxweficayqkvnb:191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f@ec2-54-225-234-165.compute-1.amazonaws.com:5432/ddtk33j69v200c", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS lawQuiz(
            answer TEXT,
            quzi TEXT
        );"""
    )
    data = pd.read_csv('data/lawQuiz.csv')
    print(data)
    data.to_sql(name='lawQuiz', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/quiz", methods = ['post'])
def quiz():
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "문제", # basic 카드에 들어갈 제목
                        "description": "000란 건물의 소유자에게 돈을 빌려 주거나 건물의 매매를 약속 하기 위해 임시등기인 가등기를 설정하는 사람을 의미합니다.000에 들어갈 단어는?", # 제목 아래에 들어갈 상세 내용
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": "가등기권자", # 버튼 1 내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "가등기", # 버튼 2 내용
                                "blockId": "오답일때" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "가등기권리자",# 버튼 3내용
                                "blockId": "오답일때" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

@app.route("/quiz2", methods = ['post'])
def quiz2():
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "문제", # basic 카드에 들어갈 제목
                        "description": "000이란 건물의 사실상의 상황을 기재하는 장부로 건축물의 소재지, 번호, 면적 등을 자세하게 기록한 문서를 의미합니다. 빈칸에 들어갈 단어는?", # 제목 아래에 들어갈 상세 내용
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": "강제경매절차", # 버튼 1 내용
                                "blockId": "오답일때" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "건축물관리대장", # 버튼 2 내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "경매대금",# 버튼 3내용
                                "blockId": "오답일때" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

@app.route("/quiz3", methods = ['post'])
def quiz3():
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "문제", # basic 카드에 들어갈 제목
                        "description": "000이란 경매를 통해서 동산 또는 부동산의 소유권을 얻게 된 사람을 말합니다. 즉, 경매에서 건물이나 물건을 낙찰 받은 사람이000입니다. 빈칸에 들어갈 단어는?", # 제목 아래에 들어갈 상세 내용
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": "낙오자", # 버튼 1 내용
                                "blockId": "정답일때" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "낙찰", # 버튼 2 내용
                                "blockId": "오답일때" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "낙찰자",# 버튼 3내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    #db_create() # 데이터 베이스 업로드
    app.run(host='0.0.0.0', port=int(args[1]),debug=True)