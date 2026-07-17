from domain.type_document import CodeTypeDocument
from infrastructure.document_repository import DocumentRepository


def executer(
    dossier_id,
    nom,
    type_document: CodeTypeDocument,
    chemin_fichier,
    taille
):
    return DocumentRepository.creer(
        dossier_id=dossier_id,
        nom=nom,
        type_document=type_document,
        chemin_fichier=chemin_fichier,
        taille=taille
    )