from flask import render_template, flash, redirect
import src.forms as forms
import src.services as services


class HomeController:
    service = services.LoanService()

    def home(self):
        form = forms.LoanForm()
        if form.validate_on_submit():
            atts = dict({key: val for key, val in form.data.items()})
            try:
                self.service.create_loan(atts)
                flash('Pedido de prestamo exitoso', 'success')
                return redirect('#loan')
            except Exception as e:
                flash(str(e), 'danger')
                return render_template('home.html', form=form)

        return render_template('home.html', form=form)


