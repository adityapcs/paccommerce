import json
import os

_DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "../data/users.json")


def load_users(db_path=_DEFAULT_DB_PATH):
    if os.path.exists(db_path):
        with open(db_path, "r") as f:
            return json.load(f)
    else:
        return{}


def save_users(users, db_path=_DEFAULT_DB_PATH):
    with open(db_path, "w") as f:
        json.dump(users, f, indent=4)


def add_user(username, tier, db_path=_DEFAULT_DB_PATH, overwrite=False):
    users = load_users(db_path)

    if username in users and not overwrite:
        raise ValueError("User already exists")

    users[username] = tier
    save_users(users, db_path)


def get_user(username, db_path=_DEFAULT_DB_PATH):
    users = load_users(db_path)
    return users.get(username)


def delete_user(username, db_path=_DEFAULT_DB_PATH):
    users = load_users(db_path)

    if username in users:
        del users[username]
        save_users(users, db_path)
        return True

    return False