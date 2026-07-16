from infrastructure.type_document_repository import TypeDocumentRepository


def executer(
    code: str,
    libelle: str,
    description: str = None,
    ordre: int = 0
):

    type_document = TypeDocumentRepository.trouver_par_code(code)

    if type_document:
        return None

    return TypeDocumentRepository.creer(
        code=code,
        libelle=libelle,
        description=description,
        ordre=ordre
    )