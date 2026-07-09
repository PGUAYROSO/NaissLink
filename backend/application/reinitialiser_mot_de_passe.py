from infrastructure.utilisateur_repository import UtilisateurRepository
from security.password import hasher


def executer(
    utilisateur_id: int,
    mot_de_passe: str
):

    utilisateur = UtilisateurRepository.trouver_par_id(
        utilisateur_id
    )

    if utilisateur is None:
        return None

    utilisateur.mot_de_passe = hasher(
        mot_de_passe
    )

    UtilisateurRepository.enregistrer()

    return utilisateur