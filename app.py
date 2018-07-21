from flask import Flask, jsonify, abort, request, render_template
import sqlite_db
import random


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bullguard/api/v1.0/users/create', methods=['POST'])
def create_table():
    sqlite_db.create_table()
    return True


@app.route('/bullguard/api/v1.0/users', methods=['GET'])
def get_users():
    users = sqlite_db.get_all_users_db()
    return jsonify({'all_users': users})


@app.route('/bullguard/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = sqlite_db.get_all_users_db()
    found = False
    for user_details in users:  # users is a list with dictionaries in it containing each user details
        if user_details['id'] == user_id:  # if the user_id requested from the user is equal to the id from the DB
            #  create new dict with all the user details
            full_details = {'user_basic_details': user_details,
                            'user_profession_details': {'work experience': 6, 'level': 'Master', 'location': 'Remote'}}
            return jsonify(full_details)
        else:
            pass
    if found is False:  # in case the id was not found, raise 404 status code
        abort(404)


@app.route('/bullguard/api/v1.0/users', methods=['POST'])
def create_user():  # relevant for POST request from curl/requests etc.
    if not request.json or 'first_name' not in request.json or \
            'last_name' not in request.json or 'role' not in request.json:
        # validate the request is in JSON format and that all the fields are not empty
        abort(400)

    # create new user in the DB
    sqlite_db.create_user_db(request.json.get('id', ""),
                             request.json.get('first_name', ""),
                             request.json.get('last_name', ""),
                             request.json.get('role', ""))

    # create new dict to display in the browser as JSON
    user = {
        'id': request.json.get('id', ""),
        'first_name': request.json.get('first_name', ""),
        'last_name': request.json.get('last_name', ""),
        'role': request.json.get('role', "")
    }

    return jsonify({'user': user}), 201


@app.route('/bullguard/api/v1.0/users/create-user', methods=['POST'])
def create_user_from_website():  # relevant for POST request from the web browser
    if not request:
        abort(400)
    random_id = random.randint(11111111, 99999999)  # generate random number for user id

    # create new user in the DB
    sqlite_db.create_user_db(random_id,
                             request.form['first_name'],
                             request.form['last_name'],
                             request.form['role'])

    # create new dict to display in the browser as JSON
    user = {
        'id': random_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'role': request.form['role']
    }

    return jsonify({'user': user}), 201


@app.route('/bullguard/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = sqlite_db.get_all_users_db()
    found = False
    for user_details in users:  # users is a list with dictionaries in it containing each user details
        if user_details['id'] == user_id:
            found = True
            user = {
                'id': user_details['id'],
                'first_name': user_details['first_name'],
                'last_name': user_details['last_name'],
                'role': user_details['role']
            }
    if found is True:
        sqlite_db.delete_user_db(user_id)
        return jsonify({'deleted_user_details': user})
    else:
        abort(404)

    return jsonify({'result': True})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
