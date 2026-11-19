from flask import Flask, render_template, request, redirect, url_for
from db import Database

app = Flask(__name__)

db = Database(host='localhost', user='root', password='admin', database='flask_auth')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = "Заполните все поля"
        else:
            user = db.get_user(username)

            if user and user['user_password'] == password:
                return redirect(url_for('login_page'))
            else:
                error = "Неверное имя пользователя или пароль"

    except Exception as e:
        print(f"Ошибка: {e}")
        error = "Произошла ошибка на сервере. Попробуйте позже."

    return render_template('index.html', error=error)


@app.route('/login_page')
def login_page():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)