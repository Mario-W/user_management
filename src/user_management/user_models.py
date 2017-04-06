from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.orm import sessionmaker
from manage import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:630131222@localhost/user_management?charset=utf8'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

session = sessionmaker(bind=app)

class User(db.Model):

    id = db.Column(db.Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.SmallInteger, nullable=True)
    sex = db.Column(db.String(2), nullable=False, default='未知')
    address = db.Column(db.String(256), nullable=True)

if __name__ == '__main__':
    manager.run()