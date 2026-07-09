from app import create_app
from app.extensions import db

from domain.utilisateur import Utilisateur
from security.password import hasher


app = create_app()


with app.app_context():

    print("===================================")
    print("Création du compte administrateur")
    print("===================================")

    utilisateur = Utilisateur.query.filter_by(
        login="pguayroso"
    ).first()

    if utilisateur:

        print("✔ L'administrateur existe déjà.")

    else:

        admin = Utilisateur(
            nom="GUAYROSO",
            prenom="Patrice",
            login="pguayroso",
            email="patrice@chbt.fr",
            mot_de_passe=hasher("Admin123!"),
            role="ADMINISTRATEUR",
            actif=True
        )

        db.session.add(admin)
        db.session.commit()

        print("✔ Administrateur créé avec succès.")