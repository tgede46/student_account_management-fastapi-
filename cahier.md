# Cahier des charges : Gestionnaire de comptes bancaires pour étudiants 🏦 

1. Introduction
Ce projet consiste à développer un système simple de gestion de comptes bancaires, destiné aux étudiants. Il permettra de gérer des comptes, effectuer des transactions et afficher des relevés bancaires en appliquant uniquement la programmation orientée objet (POO) en Python, sans utiliser de framework.

2. Objectifs
✔️ Simuler un système bancaire simplifié pour étudiants.
✔️ Permettre l'ouverture et la gestion de comptes.
✔️ Gérer les transactions : dépôts, retraits et transferts.
✔️ Générer un relevé des opérations effectuées.
✔️ Appliquer les concepts POO : encapsulation, héritage, polymorphisme.

3. Fonctionnalités
3.1 Gestion des clients (Étudiants) 👤
Création de comptes étudiants.
Consultation des informations personnelles et du solde.

3.2 Gestion des comptes bancaires 💳
Création et suppression de comptes.
Consultation du solde actuel.
Vérification des conditions (ex : solde minimum).

3.3 Gestion des transactions 💰
Dépôt : Ajouter de l’argent au compte.
Retrait : Retirer de l’argent (avec vérification du solde).
Transfert : Envoyer de l’argent vers un autre compte étudiant.
Historique : Enregistrer toutes les transactions dans un relevé.

4. Modélisation des classes en POO
Classe Client(id_client,nom,email,compte (Objet Compte))

Classe Compte(id_compte,client (Objet Client),solde,historique_transactions (Liste des Transaction))
Méthodes : depot(montant), retrait(montant), transfert(montant, compte_destinataire)

Classe Transaction(id_transaction,type (dépôt, retrait, transfert),montant,date,compte_source,compte_destinataire (si transfert)
)

5. Contraintes et Règles
⚠️ Un étudiant ne peut avoir qu’un seul compte.
⚠️ Pas de découvert autorisé (solde >= 0 après chaque opération).
⚠️ Historique des transactions stocké pour chaque compte.

6. Technologies utilisées
Python (sans framework, uniquement POO).
Stockage : Fichier texte ou base de données SQLite (optionnel).