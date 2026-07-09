from infrastructure.utilisateur_repository import UtilisateurRepository


def executer(
    utilisateur_id: int,
    nom: str,
    prenom: str,
    email: str,
    role: str,
    actif: bool
):

    utilisateur = UtilisateurRepository.trouver_par_id(utilisateur_id)

    if utilisateur is None:
        return None

    utilisateur.nom = nom
    utilisateur.prenom = prenom
    utilisateur.email = email
    utilisateur.role = role
    utilisateur.actif = actif

    UtilisateurRepository.enregistrer()

    return utilisateur