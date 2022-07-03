from flask import Flask, jsonify, request

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
