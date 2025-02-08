class Compte_destinataire:
    def __init__(self,nom,email,numero_compte):
        self.nom=nom
        self.email=email
        self.numero_compte=numero_compte
        self.transaction=[]

    def __str__(self):
        return f"Compte_destinataire(nom={self.nom}, email={self.email}, numero_compte={self.numero_compte})"
        