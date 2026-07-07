import os
from uuid import uuid4

from werkzeug.utils import secure_filename


class StockageFichiers:

    @staticmethod
    def enregistrer(fichier, dossier_destination):

        os.makedirs(dossier_destination, exist_ok=True)

        extension = os.path.splitext(fichier.filename)[1]

        nom_fichier = f"{uuid4()}{extension}"

        chemin = os.path.join(
            dossier_destination,
            secure_filename(nom_fichier)
        )

        fichier.save(chemin)

        return chemin