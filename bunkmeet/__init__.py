from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'http://bit.ly/priyanshux'
app.config['CELERY_BROKER_URL'] = 'redis://localhost'
app.config['CELERY_BACKEND'] = 'redis://localhost'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from bunkmeet import routes
