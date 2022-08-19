# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "hello"

@app.route("/user/<user_name>/<int:user_id>", methods = ['post'])
def user(user_name,user_id):
    return f"hello,{user_name}({user_id})!"

if __name__== "__main__":
    app.run(debug=True)


