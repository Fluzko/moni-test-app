from src.config import MONI_CREDENTIAL
import requests
from flask import jsonify as jsonify


class MoniAPI:
    def __init__(self):
        self.base_url = 'https://api.moni.com.ar/api/v4'
        self.headers = {'credential': MONI_CREDENTIAL}

    def get_request(self, endpoint, body=""):
        return requests.get(self.base_url + endpoint, headers=self.headers, data=body).json()

    def approve_loan(self, dni):
        url = '/scoring/pre-score/'+dni
        print(url)
        return self.get_request(url)


class MockMoniAPI:
    response = {'status': 'approve', "has_error": False}
    # response = {"status": "rejected", "has_error": False}
    # response = {"status": "error", "has_error": True}

    def approve_loan(self, dni):
        return jsonify(self.response)
