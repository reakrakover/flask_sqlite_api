import requests
import random


# # CREATE TABLE
# r = requests.post('http://localhost:5000/bullguard/api/v1.0/users/create')
# print(r.status_code)
# print(r.text)

# # CREATE USER
# first_names = [
#     'rea',
#     'hen',
#     'dror',
#     'amir',
#     'oz'
# ]
# last_names = [
#     'krakover',
#     'barak',
#     'cohen',
#     'berg',
#     'klain'
# ]
# roles = [
#     'agent',
#     'manager',
#     'sales',
# ]
# random_id = random.randint(11111111, 99999999)
# random_first_name = random.choice(first_names)
# random_last_name = random.choice(last_names)
# random_role = random.choice(roles)
#
# payload = {'id': random_id, 'first_name': random_first_name, 'last_name': random_last_name, 'role': random_role}
# r = requests.post('http://localhost:5000/bullguard/api/v1.0/users', json=payload)
# print(r.status_code)
# print(r.text)


# # GET ALL USERS
# r = requests.get('http://localhost:5000/bullguard/api/v1.0/users')
# print(r.status_code)
# print(r.text)


# # GET USER
# user_id = 43062215
# r = requests.get('http://localhost:5000/bullguard/api/v1.0/users/{}'.format(user_id))
# print(r.status_code)
# print(r.text)


# # DELETE USER
# user_id = 61230027
# r = requests.delete('http://localhost:5000/bullguard/api/v1.0/users/{}'.format(user_id))
# print(r.status_code)
# print(r.text)
