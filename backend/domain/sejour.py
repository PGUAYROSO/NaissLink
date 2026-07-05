from dataclasses import dataclass


@dataclass
class Sejour:
    numero_sejour: str
    nom_mere: str
    prenom_mere: str
    nom_enfant: str
    date_naissance: str