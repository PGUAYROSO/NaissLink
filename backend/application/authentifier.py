from infrastructure.utilisateur_repository import UtilisateurRepository
from security.password import verifier


def executer(login: str, mot_de_passe: str):

    print("======================================")
    print("Login reçu :", login)

    utilisateur = UtilisateurRepository.trouver_par_login(login)

    print("Utilisateur :", utilisateur)

    if utilisateur is None:
        print(">>> Utilisateur introuvable")
        return None

    print("Login BDD :", utilisateur.login)
    print("Hash BDD :", utilisateur.mot_de_passe)

    resultat = verifier(
        mot_de_passe,
        utilisateur.mot_de_passe
    )

    print("Résultat vérification :", resultat)
    print("======================================")

    if not resultat:
        return None

    return utilisateur