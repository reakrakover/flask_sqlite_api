Bullgard API assignment
-------------------------

## PREREQUISITES
Before you run the project, you will need to install all dependencies from the requirements.txt file
$ pip install -r requirements.txt

## RUNNING THE PROJECT
In order to run the project, run the app.py file
$ python app.py

## PROJECT INFO
The project contains:
1 Pre populated DB file - bullgard_db.db
3 python files - app.py, sqlite_db.py, builtin_requests.py
1 HTML files folder

### API structure
/bullguard/api/v1.0/users [GET] - get all users
/bullguard/api/v1.0/users/<user_id> [GET] - get user by ID
/bullguard/api/v1.0/users [POST] - create new user with curl/requests (should include first name, last name, role in JSON payload)
/bullguard/api/v1.0/users/create-user [POST] - create new user with HTML form
/bullguard/api/v1.0/users/<user_id> [DELETE] - delete user by ID


There are 2 options to get and retrieve data:
1. requests - send GET/POST/DELETE requests directly to the server.
   You can use the pre built requests in the builtin_requests.py file.
2. web browser - use localhost in the browser.
   Get All Users Data - retrieve all basic details for all users.
   Get User Details By ID - get basic details and profession details (hardcoded).
   Create New User - create new user.

   It is recommended to use JSON formatter extension in Chrome to parse the data.

TODO
API: allow user details update.
Permissions: set permissions to retrieve data based on role.
Security: build log in process so the data will be available only to signed in users.
