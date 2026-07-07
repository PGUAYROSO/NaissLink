from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


def hasher(mot_de_passe: str) -> str:
    return generate_password_hash(mot_de_passe)


def verifier(mot_de_passe: str, hash_stocke: str) -> bool:
    return check_password_hash(hash_stocke, mot_de_passe)