from flask import render_template, url_for, flash, redirect, request
import src.forms as forms
import src.services as services


class AdminController:
    loan_service = services.LoanService()
    login_service = services.LoginService()

    def login(self):
        if self.login_service.is_logged_in():
            return redirect(url_for('dashboard'))
        form = forms.LoginForm()
        if form.validate_on_submit():
            if self.login_service.login(form):
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('dashboard'))
            else:
                flash('Usuario o contrasena incorrectos', 'danger')
        return render_template('login.html', form=form)

    def logout(self):
        self.login_service.logout()
        return redirect(url_for('home'))

    def dashboard(self):
        return render_template('dashboard.html', loans=self.loan_service.get_all_loans())

    def delete_loan(self, loan_id):
        self.loan_service.delete_loan(loan_id)
        flash('Pedido de prestamo borrado', 'success')
        return redirect(url_for('dashboard'))

    def edit_loan(self, loan_id):
        form = forms.LoanForm()
        if form.validate_on_submit():
            atts_to_update = {key: val for key, val in form.data.items()}
            self.loan_service.update_loan(loan_id, atts_to_update)
            flash('Pedido de prestamo actualizado con exito', 'success')
            return redirect(url_for('dashboard'))
        if request.method == 'GET':
            loan = self.loan_service.get_loan_by_id(loan_id)
            form.fill_with_loan(loan)
        return render_template('edit_loan.html', form=form)

