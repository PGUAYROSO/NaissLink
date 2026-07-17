from app import create_app
from app.extensions import db

from domain.type_document import TypeDocument


TYPES = [

    ("DECLARATION_NAISSANCE", "Déclaration de naissance", 1),
    ("CNI_MERE", "Carte nationale d'identité mère", 2),
    ("CNI_PERE", "Carte nationale d'identité père", 3),
    ("LIVRET_FAMILLE", "Livret de famille", 4),
    ("PASSEPORT", "Passeport", 5),
    ("RECONNAISSANCE_ANTICIPEE", "Reconnaissance anticipée", 6),
    ("ACTE_MARIAGE", "Acte de mariage", 7),
    ("JUGEMENT", "Jugement", 8),
    ("AUTRE", "Autre document", 9),

]


app = create_app()

with app.app_context():

    for code, libelle, ordre in TYPES:

        existe = TypeDocument.query.filter_by(code=code).first()

        if existe:
            continue

        db.session.add(
            TypeDocument(
                code=code,
                libelle=libelle,
                description="",
                ordre=ordre,
                actif=True
            )
        )

    db.session.commit()

    print("Types de documents créés avec succès.")