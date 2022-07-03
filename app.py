from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return jsonify(message='Hello World!')


@app.route('/super_ez')
def super_ez():
    return jsonify(message='Hello from Planetary API ;)')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found!'), 404


@app.route('/params')
def params():
    name = request.args.get('name')
    if len(name) < 5:
        return jsonify(message='Your name is too short, sorry)'), 401
    return jsonify(message='Good job, man!')


@app.route('/url_vars/<string:name>')
def url_vars(name):
    if len(name) < 5:
        return jsonify(message=f'Try your best {name}!'), 401
    return jsonify(message=f'Bad job, the man who called himself {name}!')


# Database models
class User(db.Model):
    # sqlalchemy table name
    __tablename__ = 'users'

    __slots__ = ['id', 'first_name', 'last_name', 'email', 'password']

    def __init__(self):
        self.id = Column(Integer, primary_key=True)
        self.first_name = Column(String)
        self.last_name = Column(String)
        self.email = Column(String, unique=True)
        self.password = Column(String)


class Planet(db.Model):
    # sqlalchemy table name
    __tablename__ = 'planets'

    __slots__ = ['planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance']

    def __init__(self):
        self.planet_id = Column(Integer, primary_key=True)
        self.planet_name = Column(String)
        self.planet_type = Column(String)
        self.home_star = Column(String)
        self.mass = Column(Float)
        self.radius = Column(Float)
        self.distance = Column(Float)


if __name__ == '__main__':
    app.run()
