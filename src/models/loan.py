from src import db


class Loan(db.Model):
    __tablename__ = 'loan'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    monto = db.Column(db.Integer, nullable=False)
    last_editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=None)
    last_editor = db.relationship('User',  back_populates="edits")

