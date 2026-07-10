from app.extensions import db

from domain.transmission import Transmission
from domain.dossier import StatutDossier

from infrastructure.dossier_repository import DossierRepository


def executer(
    dossier_id: int,
    commune: str,
    expediteur: str,
    commentaire: str = None
):
    # Recherche du dossier
    dossier = DossierRepository.trouver_par_id(dossier_id)

    if dossier is None:
        raise ValueError("Dossier introuvable.")

    # Vérification du statut
    if dossier.statut != StatutDossier.PRET_A_TRANSMETTRE.value:
        raise ValueError(
            "Le dossier n'est pas prêt à être transmis."
        )

    # Création de la transmission
    transmission = Transmission(
        dossier_id=dossier.id,
        commune=commune,
        expediteur=expediteur,
        commentaire=commentaire
    )

    # Mise à jour du dossier
    dossier.transmettre()

    # Sauvegarde dans une seule transaction
    db.session.add(transmission)
    db.session.add(dossier)

    db.session.commit()

    return transmission