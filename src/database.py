import json

_PATH_DATA = './data/users.json'

def load_users(db_path=_PATH_DATA):
    with open(db_path,'r') as file:
        data = json.load(file)
        return data

def save_users(db_path, data=_PATH_DATA):
    with open(db_path, 'w') as file:
        json.dump(data, file)

def add_user(username, tier, db_path=_PATH_DATA):
    users = load_users(db_path)
    users[username] = tier
    save_users(db_path, users)

def get_user(username, db_path=_PATH_DATA):
    users = load_users(db_path)
    return users.get(username, None)