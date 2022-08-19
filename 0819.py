# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2 as db
import pandas as pd

@app.route("/rank", methods = ['post'])
def test():
    script = 'SELECT * FROM public."user"'
    df = pd.read_sql(script, conn)
    rank_list = df.head()
    body = request.get_json()
    print(body)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "TOP5", # basic 카드에 들어갈 제목
                        "description": rank_list,
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

if __name__== "__main__":
    app.run(debug=True)    