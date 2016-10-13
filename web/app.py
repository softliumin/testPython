#!/usr/bin/python
#coding=utf-8
from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    #return '<h1>1111</h1>'
    return render_template('/page/all.html')


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
    app.run(debug=True)