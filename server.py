# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template, redirect
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2 as db
import pandas as pd

app = Flask(__name__)

nextid = 4
topics = [
    {'id':1, 'title':'박근태','body':'박근태는 멋쟁이'},
    {'id':2, 'title':'이용수','body':'이용수는 신나요 신나'},
    {'id':3, 'title':'문호준','body':'문호준은 신중해....'}
]

def template(contents, content, id=None):
    contextUI = ''
    if id !=None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/"method="POST"><input type="submit"value="delete"></form></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        <body>    
    </html>
    '''    

def getcontents():
    litags = ''
    for topic in topics:
        litags = litags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return litags    

@app.route('/')
def index():
    return template(getcontents(),'<h2>welcome</h2>GOD is Good')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title == topic['title']
            body = topic['body']
            break
             
    return template(getcontents(), f'<h2>{title}</h2>{body}',id)    
    
@app.route('/create/',methods=['GET','POST'])
def create():
    if request.method =="GET":
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>     
        '''    
        return template(getcontents(),content)
    elif request.method == 'POST':
        global nextid
        title = request.form['title']
        body = request.form['body']
        newtopic = {'id': nextid, 'title':title, 'body':body}
        topics.append(newtopic)
        url = '/read/'+str(nextid)+'/'
        nextid = nextid + 1
        return redirect(url)

@app.route('/update/<int:id>/',methods=['GET','POST'])
def update(id):
    if request.method =="GET":
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title == topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title"value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>     
        '''    
        return template(getcontents(),content)
    elif request.method == 'POST':
        global nextid
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

@app.route('/delete/<int:id>/',methods=['POST'])
def delete(id):
    for topic in topics:
        topics.remove(topic)
        break
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True)
