from app import app
from flask import render_template
from datetime import datetime

@app.route('/')
def test():
    current_year = datetime.now().strftime("%Y")
    return render_template('test_article.html', current_year=current_year)
