from app import app
from flask import render_template
from datetime import datetime
from flask import request

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
