import random
import sqlite3
import string


from faker import Faker

import requests


fake = Faker()


def generate_random_password(password_len=10) -> str:
    chars = string.digits + string.ascii_letters + string.punctuation

    result = ""
    for _ in range(password_len):
        result += random.choice(chars)
    return result


def get_requirements_content():
    with open("requirements.txt", 'r') as file:
        content = file.read()
    return content


def generate_fake_name(name_count=100) -> str:

    result = " "
    for _ in range(name_count):
        fake_data = fake.first_name() + " " + fake.email() + " "
        result += fake_data
    return result


def get_astros():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


def exec_query(query: str) -> list:
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
