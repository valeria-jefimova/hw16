import json

def load_json(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)

        return json_data

def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)

    db.session(commit)


def dumps(param):
    return None