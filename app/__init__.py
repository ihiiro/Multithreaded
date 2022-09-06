from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '1b7d563d1f7e1e64d1bd6ba2'


from app import routes
