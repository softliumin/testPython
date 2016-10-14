#!/usr/bin/python
#coding=utf-8
from flask import Flask,render_template
from flask import request
import MySQLdb


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    #return '<h1>1111</h1>'
    # 在这里进行数据的查询和放入模板
    conn = MySQLdb.connect(
        host='101.200.145.47',
        port=3306,
        user='root',
        passwd='liumin110',
        db='liumin2',
    )


    cur=conn.cursor()
    cur.execute("select * from sss")
    result = cur.fetchall()

    return render_template('/page/all.html',name='haha',pp=result)
# cur.execute("insert into sss values(111,'huhu')")






@app.route('/login',methods=['GET'])
def login():
    return '''
            <h1>Hello ,Please Login</h1>
            <form action='/login' method='post'>
            name<input type='text' name='name'/><br/><br/>
            pwd<input type='password' name='password'/><br/><br/>
            <button  type='submit' >login</button>
            </form>
        '''
@app.route('/login',methods=['POST'])
def login2():
    if request.form['name']=='admin' and request.form['password']=='password':
        return '<h1>Hello admin</h1>'
    return '<h1>Bad Login Info</h1>'

if __name__ == '__main__':
    app.run()#debug=True