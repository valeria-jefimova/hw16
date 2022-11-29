#
import json

from config import db

# Данные джсон необходимо положить в базу данных, используя модели
# ** - распаковка данных
from main import User, Offer, Orders


def insert_data(model, data):
    for row in data:
        db.session.add(model(**row))
    db.session.commit()

  # Положить данные в базу данных
def add_data():
    # db.drop_all()
    db.create_all()
    #прочитали и сохранили
    with open('user.json', 'r', encoding='utf-8') as file:
        insert_data(User, json.load(file))

    with open('orders.json', 'r', encoding='utf-8') as file:
        insert_data(Orders, json.load(file))

    with open('offers.json', 'r', encoding='utf-8') as file:
        insert_data(Offer, json.load(file))


