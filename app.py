from flask import Flask, request

import database.updateJson

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
    else:
        return {"code": 500, "msg": "Error Methods", "data": ''}
    if database.updateJson.insert(username, passwd):
        return {"code": 200, "msg": "Success Insert ", "data": f'{username}:{passwd}'}


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
    else:
        return {"code": 500, "msg": "Error Methods", "data": ''}
    if database.updateJson.select(username) == passwd:
        return {"code": 200, "msg": "Success Login ", "data": f'Login: {username}'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=True)
