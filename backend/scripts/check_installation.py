from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


BASE_DIR = Path(__file__).resolve().parent.parent


def ok(message):
    print(f"✓ {message}")


def erreur(message):
    print(f"✗ {message}")


def verifier_env():
    env = BASE_DIR / ".env"

    if env.exists():
        ok(".env trouvé")
        return True

    erreur(".env absent")
    return False


def verifier_repertoires():

    dossiers = [
        "uploads",
        "logs",
        "backups",
        "temp"
    ]

    for dossier in dossiers:

        chemin = BASE_DIR / dossier

        if chemin.exists():
            ok(f"{dossier}")
        else:
            erreur(f"{dossier} manquant")


def verifier_postgresql():

    load_dotenv(BASE_DIR / ".env")

    url = os.getenv("DATABASE_URL")

    if not url:
        erreur("DATABASE_URL non définie")
        return

    try:

        engine = create_engine(url)

        with engine.connect() as connexion:

            connexion.execute(text("SELECT 1"))

        ok("Connexion PostgreSQL")

    except SQLAlchemyError as e:

        erreur(f"Connexion PostgreSQL ({e})")


def verifier_tables():

    load_dotenv(BASE_DIR / ".env")

    url = os.getenv("DATABASE_URL")

    if not url:
        return

    tables = [
        "utilisateurs",
        "types_documents",
        "dossiers",
        "documents",
        "transmissions",
        "audit_logs"
    ]

    try:

        engine = create_engine(url)

        with engine.connect() as connexion:

            for table in tables:

                resultat = connexion.execute(text(f"""
                    SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_name='{table}'
                    )
                """))

                existe = resultat.scalar()

                if existe:
                    ok(table)
                else:
                    erreur(table)

    except Exception as e:

        erreur(str(e))


def main():

    print("=" * 50)
    print(" Vérification de l'installation NaissLink")
    print("=" * 50)

    verifier_env()
    verifier_repertoires()
    verifier_postgresql()
    verifier_tables()

    print("=" * 50)
    print("Fin de la vérification")
    print("=" * 50)


if __name__ == "__main__":
    main()