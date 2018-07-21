import sqlite3


def create_table():
    conn = sqlite3.connect('bullgard_db.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, first_name TEXT, last_name TEXT, role TEXT)')


def get_all_users_db():
    conn = sqlite3.connect('bullgard_db.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    rows_list = []
    for row in rows:
        d = dict(zip(row.keys(), row))  # a dict with column names as keys
        rows_list.append(d)

    return rows_list


def create_user_db(id_data, first_name_data, last_name_data, role_data):
    conn = sqlite3.connect('bullgard_db.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO users (id, first_name, last_name, role) VALUES ('{}', '{}', '{}', '{}')"
                  .format(id_data, first_name_data, last_name_data, role_data))
        conn.commit()


def delete_user_db(user_id):
    conn = sqlite3.connect('bullgard_db.db')
    with conn:
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = '{}'".format(int(user_id)))
        conn.commit()
