from flask import Flask
from data.__all_models import User
from data import db_session


app = Flask(__name__)


def main():
    db_session.global_init("db/users.sqlite")

    user = User()
    user.name = "Капитан"
    user.about = "Толстяк"
    user.email = "email@capitan.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Зеленый человек"
    user.about = "Огурец"
    user.email = "email@cucumber.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Красный человек"
    user.about = "Помидор"
    user.email = "email@tomato.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Синий человек"
    user.about = "Голубика"
    user.email = "email@blueberry.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()





