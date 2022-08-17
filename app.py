# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local


app = Flask(__name__)

@app.route("/", methods = ['post'])
def index():
    return 'heee'

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




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.args[1]),debug=True)