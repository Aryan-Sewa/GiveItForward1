from flask import Flask,request,render_template,jsonify
import json


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html')

if __name__=='__main__':
    app.run(debug=True)