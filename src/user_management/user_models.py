from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysqldb://localhost/user_management?charset=utf8'
db = SQLAlchemy(app)
class User(db.Model):

    name = db.Column()
    age = db.Column()
    sex = db.Column()
    address = db.Column()
