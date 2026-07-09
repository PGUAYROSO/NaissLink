import subprocess
import sys

print("======================================")
print("Bootstrap NaissLink")
print("======================================")

subprocess.run(
    [sys.executable, "scripts/init_admin.py"]
)

print("======================================")
print("Bootstrap terminé.")
print("======================================")