import sqlite3
from collections import Counter

from flask import Flask, request


from utils import exec_query, generate_fake_name, generate_random_password, get_astros, get_requirements_content


app = Flask(__name__)


@app.route('/generate_password/')
def generate_password():
    password_len = request.args.get('password-len', '10')

    if not password_len.isdigit():
        return "Error, password-len should be integer"

    password_len = int(password_len)

    if password_len > 100:
        return "Password should be less than 100"

    return generate_random_password(password_len)


@app.route('/requirements/')
def requirements():
    return get_requirements_content()


@app.route('/generate-users/')
def fake_name():
    name_count = request.args.get('name-count', '100')

    if not name_count.isdigit():
        return "Error, name-count should be integer"

    name_count = int(name_count)

    if name_count > 200:
        return "Should be less than 200"

    return generate_fake_name(name_count)


@app.route('/space/')
def space():
    return get_astros()


@app.route('/customers/')
def customers():
    country = request.args['country']
    query = f"SELECT * FROM customers WHERE Country = '{country}';"
    return str(exec_query(query))


@app.route('/customers_all/')
def customers_all():
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute('Select * from customers;')
    result = cursor.fetchall()
    conn.close()
    return str(result)


@app.route('/invoices/')
def invoices():
    query = 'SELECT * FROM invoices;'
    return str(exec_query(query))


@app.route('/names/')
def customers_names():
    query = 'SELECT FirstName FROM customers;'
    name_list = str(exec_query(query))
    result = Counter(name_list).values()
    return str(result)


@app.route('/tracks/')
def tracks():
    query = 'SELECT COUNT(TrackId) FROM tracks;'
    return str(exec_query(query))


@app.route('/tracks-sec/')
def tracks_sec():
    query = 'SELECT Name, Milliseconds/1000 FROM tracks;'
    return str(exec_query(query))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
