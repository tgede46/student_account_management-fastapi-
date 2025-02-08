from client import Client

class Transaction:
    def __init__(self, montant, date,client:Client):
        self.montant = montant
        self.date = date

    def __str__(self):
        return f"Transaction(montant={self.montant}, date={self.date})"
    