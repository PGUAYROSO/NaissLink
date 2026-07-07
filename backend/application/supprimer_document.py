import os

from infrastructure.document_repository import DocumentRepository


def executer(document):

    if os.path.exists(document.chemin_fichier):
        os.remove(document.chemin_fichier)

    DocumentRepository.supprimer(document)