from app import db
from sqlalchemy.dialects.postgresql import JSON


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
