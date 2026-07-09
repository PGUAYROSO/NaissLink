from app import create_app
from app.extensions import db

from domain.utilisateur import Utilisateur
from security.password import hasher


app = create_app()


with app.app_context():

    utilisateur = Utilisateur.query.filter_by(
        login="pguayroso"
    ).first()

    if utilisateur is None:

        print("Utilisateur introuvable.")

    else:

        utilisateur.mot_de_passe = hasher("Admin123!")

        db.session.commit()

        print("Mot de passe réinitialisé.")