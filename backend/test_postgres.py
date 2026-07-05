import psycopg2
import traceback

print("START")

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="naisslink",
        user="postgres",
        password="postgres"
    )

    print("CONNECTED")

    cur = conn.cursor()
    cur.execute("SELECT current_database();")
    print(cur.fetchone())

    conn.close()

except Exception:
    traceback.print_exc()