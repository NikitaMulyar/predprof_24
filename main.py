from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.user import RegisterForm, LoginForm
from data import db_session
from data.users import User

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
    options = {1: "asdf", 2: "fda"}  # ДАТЫ
    date = 0
    if request.method == "POST":
        date = request.form.get('xxx')
        print(date)
    data = []
    # if date == 0:
    #     for el in options.values():
    #         data.append(func(el)) # по дате получаем окна
    # else:
    #     data.append(func(options[date]))  # по дате получаем окна
    data.append([[(1, 1), (1, 0), (2, 0)], [(3, 0), (3, 1), (3, 1)], [(4, 1), (4, 0), (5, 0)]][::-1])
    print(data)
    return render_template('index.html', option=options, dates=data)


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
def add():
    return render_template('rooms.html', title='Комнаты')


if __name__ == '__main__':
    db_session.global_init("db/database.db")
    app.run(port=int(port), host=host)
