from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Participant(db.Model):
    __tablename__ = 'participant'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String())
    lname = db.Column(db.String())
    track = db.Column(db.String())
    height = db.Column(db.Integer)
    marvel = db.Column(db.Integer)
    pet = db.Column(db.Integer)

    def __init__(self, fname,lname, track, height, marvel, pet):
        self.fname = fname
        self.lname = lname
        self.track = track
        self.height = height
        self.marvel = marvel
        self.pet = pet

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route('/add', methods=['GET'])
def add():
    print(5)
    if request.method == 'POST':
        db.session.add(Participant(
            request.args.get('fname'),
            request.args.get('lname'),
            request.args.get('track'),
            request.args.get('height'),
            request.args.get('marvel'),
            request.args.get('height')
        ))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}



if __name__ == '__main__':
    app.run()
