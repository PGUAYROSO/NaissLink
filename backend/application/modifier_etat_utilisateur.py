from infrastructure.utilisateur_repository import UtilisateurRepository


def executer(
    utilisateur_id: int,
    actif: bool
):

    utilisateur = UtilisateurRepository.trouver_par_id(
        utilisateur_id
    )

    if utilisateur is None:
        return None

    utilisateur.actif = actif

    UtilisateurRepository.enregistrer()

    return utilisateur