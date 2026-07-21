from app.extensions import db
from domain.historique_transmission import (HistoriqueTransmission)
from infrastructure.historique_transmission_repository import (HistoriqueTransmissionRepository)

def executer(
    transmission_id,
    utilisateur,
    action,
    commentaire=None
):

    historique = HistoriqueTransmission(

        transmission_id=transmission_id,

        utilisateur=utilisateur,

        action=action,

        commentaire=commentaire

    )

    HistoriqueTransmissionRepository.ajouter(
        historique
    )

    return historique