from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.user import RegisterForm, LoginForm
from data import db_session
from data.users import User
from forms.juri import JuriForm
import json
from funcs_back import *
from db_funcs import *
import pprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
host = '127.0.0.1'
port = '5000'
path = f'http://{host}:{port}'


# ГЛАВНАЯ СТРАНИЦА
@app.route('/', methods=['GET', 'POST'])
def index():
    options = {i + 1: el for i, el in enumerate(get_all_dates())}
    date = 0
    if request.method == "POST":
        date = int(request.form.get('xxx'))
    data = []
    if date == 0:
        for el2 in options.values():
            el = el2.split('-')
            el[-1] = '20' + el[-1]
            el = "-".join(el)
            el = datetime.datetime.strptime(el, "%d-%m-%Y")
            data.append(make_matrix_for_windows(el)[::-1]) # по дате получаем окна
        choose_date = list(options.values())
    else:
        el = options[date]
        el = el.split('-')
        el[-1] = '20' + el[-1]
        el = "-".join(el)
        el = datetime.datetime.strptime(el, "%d-%m-%Y")
        data.append(make_matrix_for_windows(el)[::-1])  # по дате получаем окна
        choose_date = [options[date]]

    return render_template('index.html', option=options, dates=data, choose_date=choose_date)


# ТУТ БУДЕТ ЛИЧНАЯ СТРАНИЧКА ПОЛЬЗОВАТЕЛЯ
@app.route('/user')
def user():
    return render_template('user.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# ЛОГИНИМСЯ
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


# РЕГИСТРАЦИЯ
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            login=form.login.data,
            surname=form.surname.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# ВЫХОДИМ ИЗ АККА
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/rooms', methods=['GET'])
def rooms_html():
    return render_template('rooms.html', title='Комнаты')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = JuriForm()
    if form.validate_on_submit():
        try:
            data = form.body.data
            json_acceptable_string = data.replace("'", "\"")
            data = json.loads(json_acceptable_string)
            res = rooms(data)
            date = res["date"]
            print(date)
            for w in res['windows']:
                put_to_db_windows(date, res['windows'][w], w[0], w[1])
                put_to_db_room(date, w[1], len(res['windows'][w]))
        except Exception:
            return render_template('mistake.html')
    return render_template('add.html', form=form)


if __name__ == '__main__':
    db_session.global_init("db/site.db")
    app.run(port=int(port), host=host)
