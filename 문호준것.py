# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2 as db
import pandas as pd

conn_string="dbname='ddtk33j69v200c' host='ec2-54-225-234-165.compute-1.amazonaws.com' user='uxweficayqkvnb' password='191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f'"
conn=db.connect(conn_string)
script = "SELECT * FROM law"
df = pd.read_sql(script, conn)
print(df.head())

#문제와 정답만들기
result = df.sample(3)
print(result)
#우선 용어와 설명 분리
result = np.array(result)

app = Flask(__name__)

@app.route("/test1", methods = ['post'])
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
                        "description": result[0,1]
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": result[0,0], # 버튼 1 내용
                                "blockId": "정답일때테스트" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": result[1,0], # 버튼 2 내용
                                "blockId": "오답일때테스트" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": result[2,0],# 버튼 3내용
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
                        "description": result[1,1]
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

@app.route("/test3", methods = ['post'])
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
                        "description": result[2,0]
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": result[0,0], # 버튼 1 내용
                                "blockId": "오답일때테스트" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": result[1,0], # 버튼 2 내용
                                "blockId": "오답일때테스트" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": result[2,0]",# 버튼 3내용
                                "blockId": "정답일때테스트" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__== "__main__":
    app.run()
