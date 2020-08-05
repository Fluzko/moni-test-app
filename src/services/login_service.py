import src.models as model
from src import bcrypt
from flask_login import login_user, current_user, logout_user


class LoginService:

    @staticmethod
    def is_logged_in():
        return current_user.is_authenticated

    @staticmethod
    def login(form):
        user = model.User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)

    @staticmethod
    def logout():
        logout_user()
