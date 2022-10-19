import json
from main import app, User


@app.route("/users")
def get_users():
        user_list = User.query.all()

        user_response = []

        for user in user_list:
            user_response.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            })

        return json.dumps(user_response)


@app.route("/users/<int:uid>")
def get_user(uid):
    user = User.query.get(uid)
    return json.dumps({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    })

@app.route("/orders")
def get_orders():
        order_list = Order.query.all()

        order_response = []

        for order in order_list:
            order_response.append({
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_name,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price
            })

        return json.dumps(order_response)


@app.route("/orders/<int:uid>")
def get_order(uid):
    order = Order.query.get(uid)
    return json.dumps({
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_name,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price
    })

@app.route("/offers")
def get_offers():
        offer_list = Offer.query.all()

        offer_response = []

        for offer in offer_list:
            offer_response.append({
                "id": offer.id,
            })

        return json.dumps(order_response)


@app.route("/offers/<int:uid>")
def get_offer(uid):
    offer = Offer.query.get(uid)
    return json.dumps({
        "id": offer.id,
    })
