from app import app
from flask import render_template
from datetime import datetime
from flask import request

@app.route('/')
def test():
    return render_template('test_article.html',
                           current_year=datetime.now().strftime("%Y"),
                           request_url=request.url)

@app.route('/home')
def home():
    return render_template('home.html',
                           current_year=datetime.now().strftime("%Y"),
                           request_url=request.url)
