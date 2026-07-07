from infrastructure.utilisateur_repository import UtilisateurRepository
from security.password import verifier


def executer(login: str, mot_de_passe: str):

    utilisateur = UtilisateurRepository.trouver_par_login(login)

    if utilisateur is None:
        return None

    if not verifier(
        mot_de_passe,
        utilisateur.mot_de_passe
    ):
        return None

    return utilisateur