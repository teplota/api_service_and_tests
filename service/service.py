#!flask/bin/python

from flask import Flask, jsonify, abort, request, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users = []


@app.errorhandler(404)
def not_found_404(error):
    return jsonify(error=str('Not found')), 404


@app.errorhandler(400)
def bad_request_400(error):
    return jsonify(error=str('Bad Request')), 400


@app.errorhandler(500)
def server_error_500(error):
    return jsonify(error=str('Server Error')), 500


def make_public_user(user):
    new_user = {}
    for field in user:
        if field == 'id':
            new_user['uri'] = url_for('get_user', user_id=user['id'], _external=True)
        else:
            new_user[field] = user[field]
    return new_user


@app.route('/service/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if not user:
        abort(404)
    return jsonify({'user': user[0]})


@app.route('/service/api/v1.0/users', methods=['GET'])
def get_users():
    return jsonify({'users': list(map(make_public_user, users))})


@app.route('/service/api/v1.0/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json or 'surname' not in request.json:
        abort(400)
    else:
        id = len(users) + 1
        user = {
            'id': id,
            'name': request.json['name'],
            'surname': request.json['surname']
        }
        users.append(user)
        return jsonify({'user': user}), 201


if __name__ == '__main__':
    app.run(debug=True)
