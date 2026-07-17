import platform
import sys
from pathlib import Path

from app.extensions import db


def executer():
    return {
        "application": "NaissLink",
        "version": "1.0.0",
        "python": sys.version.split()[0],
        "systeme": platform.system(),
        "version_os": platform.release(),
        "architecture": platform.machine(),
        "base_de_donnees": db.engine.name,
        "repertoire": str(Path.cwd())
    }