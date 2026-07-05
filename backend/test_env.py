import psycopg2
import traceback

try:
    print("Début du test...")

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="naisslink",
        user="postgres",
        password="postgres"
    )

    print("Connexion OK")

except Exception:
    traceback.print_exc()