class Client:
    def __init__(self,id_client, nom, email, comptes):
        self.id_client = id_client
        self.nom = nom
        self.email = email
        self.comptes = comptes

    

    def presentation(self):
        return f"Bonjour, je suis {self.nom} avec l'email {self.email} et je suis client de la banque"