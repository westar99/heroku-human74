# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2 as db
import pandas as pd

## DB 연결 Local
conn_string="dbname='ddtk33j69v200c' host='ec2-54-225-234-165.compute-1.amazonaws.com' user='uxweficayqkvnb' password='191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f'"
conn=db.connect(conn_string)
script = 'SELECT * FROM public."LQ1"'
df = pd.read_sql(script, conn)
print(df.head())

app = Flask(__name__)

@app.route("/quiz", methods = ['post'])
def quiz():
    #문제와 정답만들기
    result = df.sample(3)
    print(result)
    result = np.array(result)

    q1 = result[0,1]
    a1 = result[0,0]
    a2 = result[1,0]
    a3 = result[2,0]
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                       "title": "문제", # basic 카드에 들어갈 제목
                        "description": q1,
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": a1, # 버튼 1 내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": a2, # 버튼 2 내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": a3,# 버튼 3내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 3에서 연결될 버튼 주소
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
    #문제와 정답만들기
    result = df.sample(3)
    print(result)
    result = np.array(result)

    q1 = result[0,1]
    a1 = result[0,0]
    a2 = result[1,0]
    a3 = result[2,0]

    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "문제", # basic 카드에 들어갈 제목
                        "description": q1,
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": a2, # 버튼 1 내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": a1, # 버튼 2 내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": a3,# 버튼 3내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 3에서 연결될 버튼 주소
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
    #문제와 정답만들기
    result = df.sample(3)
    print(result)
    result = np.array(result)

    q1 = result[0,1]
    a1 = result[0,0]
    a2 = result[1,0]
    a3 = result[2,0]

    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                       "title": "문제", # basic 카드에 들어갈 제목
                        "description": q1,
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": a2, # 버튼 1 내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": a3, # 버튼 2 내용
                                "blockId": "62fdef11745ef634f048234e" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": a1, # 버튼 3내용
                                "blockId": "62fdef0c8a1240569898e13d" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

# 랭킹 버튼 누르면 들어가지는 코드
@app.route("/rank", methods = ['post'])
def rank():
    rankscript = 'SELECT * FROM public."user"'
    rankdata = pd.read_sql(rankscript, conn)
    ranklist = rankdata.head()
    body = request.get_json()
    
    ranklist = np.array(ranklist)
    rank1 = ranklist[0,0]
    rank2 = ranklist[1,0]
    rank3 = ranklist[2,0]

    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "TOP5", # basic 카드에 들어갈 제목
                        "description": rank1 + rank2 + rank3,
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": "처음으로", # 버튼 1 내용
                                "blockId": "오답일때테스트" # 버튼 1에서 연결될 버튼 주소
                            },
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    #db_create() # 데이터 베이스 업로드
    app.run(debug=True)