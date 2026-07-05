import psycopg

print("START")

conn = psycopg.connect(
    host="localhost",
    dbname="naisslink",
    user="postgres",
    password="postgres"
)

print("CONNECTED")

with conn.cursor() as cur:
    cur.execute("SELECT current_database();")
    print(cur.fetchone())

conn.close()

print("END")