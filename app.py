from flask import Flask, render_template, request, redirect, url_for
from db import Database

app = Flask(__name__)

db = Database(host='127.0.0.1', user='root', password='admin', database='flask_auth')

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
        error = "Произошла ошибка на сервере."

    return render_template('index.html', error=error)

@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    error = None
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = "Заполните все поля"
        else:
            success = db.create_user(username, password)
            if success:
                return redirect(url_for('index'))
            else:
                error = "Пользователь с таким именем уже существует"

    except Exception as e:
        print(f"Ошибка: {e}")
        error = "Произошла ошибка на сервере."

    return render_template('register.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
