# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2 as db
import pandas as pd

conn_string="dbname='decu4p6ukv8jdg' host='ec2-3-219-52-220.compute-1.amazonaws.com' user='snfsbddylkrufb' password='65409721482aeb22b8a3966760155a940613049c8d903a4938c69e811f1993fe'"
conn=db.connect(conn_string)
script = 'SELECT * FROM public."LQ"'
df = pd.read_sql(script, conn)
print(df.head())

#문제와 정답만들기
result = df.sample(3)
print(result)
#우선 용어와 설명 분리
result = np.array(result)

app = Flask(__name__)

 

@app.route('/')
def index():
    return "GOD IS LOVE"
    
    
@app.route("/test", methods = ['post'])
def test():
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
                                "blockId": "정답일때테스트" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "가등기", # 버튼 2 내용
                                "blockId": "오답일때테스트" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "가등기권리자",# 버튼 3내용
                                "blockId": "오답일때테스트" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)


@app.route("/test2", methods = ['post'])
def test2():
    global result
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "문제", # basic 카드에 들어갈 제목
                        "description": result[1,1],
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": result[0,0], # 버튼 1 내용
                                "blockId": "62ff09709465de0507b218b2" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": result[1,0], # 버튼 2 내용
                                "blockId": "62ff0801745ef634f048330f" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": result[2,0],# 버튼 3내용
                                "blockId": "62ff09709465de0507b218b2" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)



if __name__== "__main__":
    app.run(debug=True)
