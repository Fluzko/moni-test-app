from src.services.moniAPI import MoniAPI as Moni, MockMoniAPI as Mock


class MoniAdapter:
    def __init__(self):
        # self.api = Moni()
        self.api = Mock()

    def approve_loan(self, dni):
        return self.api.approve_loan(dni)
