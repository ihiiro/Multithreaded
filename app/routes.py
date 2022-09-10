from app import app
from datetime import datetime
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

@app.route('/home-list<int:num>')
def home(num):
    return render_template(f'home{num}.html',
    current_year=datetime.now().strftime("%Y"),
    request_url=request.url)

@app.route('/article<int:num>')
def article(num):
    return render_template(f'article{num}.html',
                           current_year=datetime.now().strftime("%Y"),
                           request_url=request.url)

@app.route('/')
def home_redirect():
    return redirect(url_for('home', num=1))
