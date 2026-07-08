from infrastructure.audit_repository import AuditRepository


def executer(
    utilisateur: str,
    action: str,
    objet: str = None,
    adresse_ip: str = None
):

    return AuditRepository.enregistrer(
        utilisateur=utilisateur,
        action=action,
        objet=objet,
        adresse_ip=adresse_ip
    )