from flask_login import login_required
from src import app
import src.controllers as controllers


@app.route("/", methods=['GET', 'POST'])
def home():
    return controllers.HomeController().home()


@app.route("/login", methods=['GET', 'POST'])
def login():
    return controllers.AdminController().login()


@app.route("/logout")
@login_required
def logout():
    return controllers.AdminController().logout()


@app.route("/dashboard", methods=['GET'])
@login_required
def dashboard():
    return controllers.AdminController().dashboard()


@app.route("/loan/delete/<int:loan_id>", methods=['POST'])
@login_required
def delete_loan(loan_id):
    return controllers.AdminController().delete_loan(loan_id)


@app.route("/loan/edit/<int:loan_id>", methods=['GET', 'POST'])
@login_required
def edit_loan(loan_id):
    return controllers.AdminController().edit_loan(loan_id)
