import json
import time

from flask import Flask, request, send_file

app = Flask(__name__)

p = [29**i for i in range(100)]


def h(x):
    res = 0
    for i in range(len(x)):
        res += ord(x[i]) * p[i]
    return res


@app.route("/")
def download_messenger():
    return '<b>Here you will be able to download messenger\n</b>' \
           + '<a href="/download">Download</a>', 200


@app.route("/download")
def download_file():
    filename = 'myMessenger.exe'
    return send_file(filename_or_fp=filename, as_attachment=True)


@app.route("/register", methods=['POST'])
def register():
    new_data = request.json

    with open("database.json", "r") as db:
        data = json.load(db)

    if new_data['username'] in data['usernames']:
        return {'error': 'username exists'}
    else:
        data['usernames'].append(new_data['username'])
        data['users'][new_data['username']] = {'password': h(new_data['password'])}
        with open("database.json", "w") as db:
            json.dump(data, db, indent=4)
            return {'error': None}


@app.route("/authorize", methods=['POST'])
def authorize():
    new_data = request.json
    username = new_data['username']
    password = h(new_data['password'])

    with open('database.json', 'r') as db:
        data = json.load(db)

    if not(username in data['usernames']):
        return {'error': 'no such username'}

    if data['users'][username]['password'] == password:
        return {'error': None}

    return {'error': 'wrong password'}


@app.route("/search", methods=['GET'])
def search():
    search_data = request.json
    username = search_data['username']

    with open('database.json', 'r') as db:
        data = json.load(db)

    if username in data['usernames']:
        info = data['users'][username]
        return info

    return {'error': 'no such username'}


@app.route("/send_message", methods=['POST'])
def send_message():
    message_data = request.json
    message_data['timestamp'] = time.time()
    username = message_data['from']
    to = message_data['to']

    with open('database.json', 'r') as db:
        data = json.load(db)

    if username not in data['chats'].keys():
        data['chats'][username] = dict()
    if to not in data['chats'].keys():
        data['chats'][to] = dict()
    if to not in data['chats'][username].keys():
        data['chats'][username][to] = list()
    if username not in data['chats'][to].keys():
        data['chats'][to][username] = list()

    data['chats'][username][to].append(message_data)
    data['chats'][to][username].append(message_data)

    with open('database.json', 'w') as db:
        json.dump(data, db, indent=4)

    return {'ok': True}


@app.route("/get_chats", methods=['GET'])
def get_chats():
    username = request.args['username']

    with open('database.json', 'r') as db:
        data = json.load(db)

    chats = []
    if username in data['chats'].keys():
        for i in data['chats'][username].keys():
            chats.append(i)
    return {'chats': chats}


@app.route("/get_messages", methods=['GET'])
def get_messages():
    messages_data = request.json
    after_timestamp = messages_data['after_timestamp']
    user1 = messages_data['user1']
    user2 = messages_data['user2']
    limit = 100
    after_id = 0

    with open('database.json', 'r') as db:
        data = json.load(db)
    messages = []
    if user1 in data['chats'].keys() and user2 in data['chats'][user1].keys():
        messages = data['chats'][user1][user2]
    for message in messages:
        if message['timestamp'] > after_timestamp:
            break
        after_id += 1

    return {'messages': messages[after_id:after_id+limit]}


if __name__ == "__main__":
    app.run()
