"""
Simulateur du DPI.

Ce module remplace temporairement Hexagone Easily
durant le développement.
"""

from domain.sejour import Sejour

SEJOURS = {
    "202600001": Sejour(
        numero_sejour="202600001",
        nom_mere="MARTIN",
        prenom_mere="Julie",
        nom_enfant="Emma",
        date_naissance="2026-06-22"
    ),
    "202600002": Sejour(
        numero_sejour="202600002",
        nom_mere="DUPONT",
        prenom_mere="Sophie",
        nom_enfant="Lucas",
        date_naissance="2026-06-23"
    )
}


def rechercher_par_numero(numero_sejour: str):
    return SEJOURS.get(numero_sejour)