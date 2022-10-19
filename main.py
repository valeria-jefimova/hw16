from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    db.create_all()


class Offer(db. Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)

db.create_all()
session = db.session()

# Создаем внешние поля для связей между моделями
#customer_id = db.Column(db.Integer, ForeignKey("user.id"))
#executor_id = db.Column(db.Integer, ForeignKey("user.id"))
# Создаем интерфейсы для связей, указывая каждому внешние ключи
#customer = db.relationship("User", foreign_keys=[customer_id])
#executor = db.relationship("User", foreign_keys=[executor_id])





if __name__ == '__main__':
    app.run(debug=True)