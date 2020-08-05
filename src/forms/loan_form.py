from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError, NumberRange


class LoanForm(FlaskForm):
    _required = 'Requerido'
    _incorrect_dni = 'Dni incorrecto'
    nombre = StringField('Nombre', validators=[DataRequired(_required)])
    apellido = StringField('Apellido', validators=[DataRequired(_required)])
    dni = IntegerField('DNI', validators=[DataRequired(_required), NumberRange(min=0, max=99999999, message=_incorrect_dni)])
    genero = SelectField('Genero', choices=[(1, 'Masculino'), (0, 'Femenino')])
    email = EmailField('Email', validators=[DataRequired(_required)])
    monto = IntegerField('Monto', validators=[DataRequired(_required)])
    submit = SubmitField('Enviar')

    def validate_nombre(self, nombre):
        if any(char.isdigit() for char in nombre.data):
            raise ValidationError('Formato incorrecto')

    def validate_apellido(self, apellido):
        if any(char.isdigit() for char in apellido.data):
            raise ValidationError('Formato incorrecto')

    def fill_with_loan(self, loan):
        self.nombre.data = loan.nombre
        self.apellido.data = loan.apellido
        self.dni.data = loan.dni
        self.email.data = loan.email
        self.genero.data = loan.genero
        self.monto.data = loan.monto

