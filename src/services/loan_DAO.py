import src.models as models
from src.services.DAO import DAO


class LoanDAO:
    base_dao = DAO()

    def get_by_id(self, object_id):
        return self.base_dao.get_by_id(models.Loan, object_id)

    def get_all(self):
        return self.base_dao.get_all(models.Loan)

    def delete_by_id(self, object_id):
        self.base_dao.delete_by_id(models.Loan, object_id)

    def create(self, attrs_dict):
        self.base_dao.create(models.Loan, attrs_dict)

    def update(self, object_id, attrs_dict):
        self.base_dao.update(models.Loan, object_id, attrs_dict)
