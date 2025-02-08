from client import Client
from compte_destinataire import Compte_destinataire
 
#  creation de la classe Compte_client
class Compte_client:
    def __init__(self,id_compte,client:Client.nom,solde_client):
        self.id_compte=id_compte
        self.client=client
        self.solde_client=solde_client
        self.transaction=[]

# methode pour le depot de l'argent sur le compte
    def depot(self, montant):
        self.solde_client+= montant
        self.transaction.append(f"Depot de {montant} FCFA")
        return self.solde_client
    

# methode pour le retrait de l'argent sur le compte
    def retrait(self,montant):
        self.solde_client-= montant
        self.transaction.append(montant)
        return 

# methode pour le transfert de l'argent sur le compte
    def transfert(self,montant,compte_destinataire):
        if self.solde_client >= montant and self.solde_client> 1000:
            self.solde_client -=montant
            compte_destinataire += montant
            return f"Transfert de {montant} FCFA vers le compte de {compte_destinataire} a ete effectue avec succes\n Votre nouveau solde est de {self.solde_client} FCFA"
        else:
            return "Le solde de votre compte est insuffisant pour effectuer cette operation"
    
# methode pour l'affichage de l'etat du compte
    def etat(self):
        if self.solde_client <= 1000:
            return f"Le solde du compte de {self.client} est de {self.solde_cl} FCFA. Attention, votre solde est inferieur a 1000 FCFA"
        elif self.solde_client > 1000000:
            return f"Le solde du compte de {self.client} est de {self.solde_client} FCFA. Vous etes millionnaire"
        else:
            return f"Le solde du compte de {self.client} est de {self.solde_client} FCFA"
        