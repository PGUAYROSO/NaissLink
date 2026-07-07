from security.password import hasher

from domain.utilisateur import Utilisateur
from infrastructure.utilisateur_repository import UtilisateurRepository


def executer(
    nom: str,
    prenom: str,
    login: str,
    email: str,
    mot_de_passe: str,
    role: str
):

    if UtilisateurRepository.trouver_par_login(login):
        raise ValueError("Ce login existe déjà.")

    if UtilisateurRepository.trouver_par_email(email):
        raise ValueError("Cette adresse e-mail existe déjà.")

    utilisateur = Utilisateur(
        nom=nom,
        prenom=prenom,
        login=login,
        email=email,
        mot_de_passe=hasher(mot_de_passe),
        role=role
    )

    return UtilisateurRepository.creer(utilisateur)