from flask import Flask, request

from utils import generate_fake_name, generate_random_password, get_astros, get_requirements_content


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


if __name__ == "__main__":
    app.run(port=5000, debug=True)
