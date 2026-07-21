from domain.transmission import Transmission
from infrastructure.dossier_repository import DossierRepository
from infrastructure.transmission_repository import TransmissionRepository
from application.ajouter_historique_transmission import (
    executer as ajouter_historique
)
from app.extensions import db


def executer(
    numero_sejour,
    destinataire,
    mode,
    commentaire,
    cree_par
):

    try:

        dossier = DossierRepository.trouver_par_numero_sejour(
            numero_sejour
        )

        if dossier is None:
            raise ValueError(
                "Le dossier documentaire est introuvable."
            )

        transmission = Transmission(

            dossier_id=dossier.id,

            destinataire=destinataire,

            mode=mode,

            commentaire=commentaire,

            cree_par=cree_par,

            statut="EN_ATTENTE"

        )

        TransmissionRepository.creer(transmission)

        ajouter_historique(

            transmission_id=transmission.id,

            utilisateur=cree_par,

            action="Transmission créée",

            commentaire=commentaire

        )

        db.session.commit()

        return transmission

    except Exception:

        db.session.rollback()

        raise