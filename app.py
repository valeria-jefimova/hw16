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
