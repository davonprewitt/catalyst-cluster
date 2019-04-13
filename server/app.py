from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        content = request.get_json()
        instance = \
        content['fname'] + ',' + content['lname'] + ',' \
        + content['track'] + ',' \
        + content['height'] + ',' + content['marvel'] + ',' + content['pet']
        f = open("../client/data.csv", "a")
        f.write(instance + '\n')
        f.close()
    return json.dumps({'success':True})
    #, 302, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run()
