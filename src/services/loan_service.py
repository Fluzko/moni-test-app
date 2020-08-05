from src.services import loan_DAO
from src.models.moniAdapter import MoniAdapter
from flask_login import current_user


class LoanService:
    loan_dao = loan_DAO.LoanDAO()

    def get_all_loans(self):
        return self.loan_dao.get_all()

    def get_loan_by_id(self, loan_id):
        return self.loan_dao.get_by_id(loan_id)

    def delete_loan(self, loan_id):
        self.loan_dao.delete_by_id(loan_id)

    def update_loan(self, loan_id, atts_to_update_dict):
        atts_to_update_dict.update({'last_editor_id': current_user.id})
        self.loan_dao.update(loan_id, atts_to_update_dict)

    def create_loan(self, atts_dict):
        dni = atts_dict['dni']
        r = MoniAdapter().approve_loan(dni).json
        if not r['has_error']:
            if r['status'] == 'approve':
                self.loan_dao.create(atts_dict)
            else:
                raise Exception('Pedido de prestamo no aprobado')
        else:
            raise Exception('Servicio no disponible actualmente')
