from flask import Flask
from flask import request

import sample.service

app = Flask(__name__)

@app.route('/user/register', methods=['POST'])
def register():
    email = request.get_json()['email']
    keywords = request.get_json()['keywords']
    sample.service.register(email, keywords)
    return ''


@app.route('/user/<email>/add-keyword', methods=['POST'])
def add_keyword(email):
    keywords = request.get_data()
    sample.service.add_keyword(email, keywords)
    return ''


@app.route('/user/<email>/search', methods=['GET'])
def search(email):
    sample.service.search(email)
    return ''


if __name__ == '__main__':
    app.run()

