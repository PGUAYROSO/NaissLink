import os
import secrets
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    # ------------------------------------------------------------------
    # Flask
    # ------------------------------------------------------------------

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        secrets.token_hex(32)      # 64 caractères hexadécimaux (256 bits)
    )

    # ------------------------------------------------------------------
    # Base de données
    # ------------------------------------------------------------------

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ------------------------------------------------------------------
    # Upload des documents
    # ------------------------------------------------------------------

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "..",
        os.getenv("UPLOAD_FOLDER", "uploads")
    )

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024      # 20 Mo

    # ------------------------------------------------------------------
    # JWT
    # ------------------------------------------------------------------

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        secrets.token_hex(32)      # 64 caractères hexadécimaux (256 bits)
    )

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)