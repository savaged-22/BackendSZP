# db/mongo.py
from __future__ import annotations

import os
from typing import Optional
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database

# Cargar .env una sola vez
load_dotenv()

_MONGO_URL = (
    os.getenv("MONGODB_URL")
    or os.getenv("DATABASE_URL")        # alias opcional
)
_DB_NAME = os.getenv("MONGODB_DB", "SafeZonePet")

# Cachés de módulo (singleton)
_client: Optional[MongoClient] = None
_db: Optional[Database] = None


class Connection:
    """Singleton sencillo para exponer DB de MongoDB."""

    @staticmethod
    def get_client() -> MongoClient:
        global _client
        if _client is not None:
            return _client

        if not _MONGO_URL:
            raise RuntimeError(
                "No se encontró MONGODB_URL (o DATABASE_URL) en el entorno."
            )

        # Configura timeouts razonables; ServerApi v1 para Atlas
        _client = MongoClient(
            _MONGO_URL,
            server_api=ServerApi("1"),
            serverSelectionTimeoutMS=5000,  # 5s
            connectTimeoutMS=5000,          # 5s
            retryWrites=True,
        )

        # Verifica conexión (lanza excepción si falla)
        _client.admin.command("ping")
        return _client

    @staticmethod
    def get_db() -> Database:
        global _db
        if _db is not None:
            return _db
        client = Connection.get_client()
        _db = client[_DB_NAME]
        return _db

    @staticmethod
    def close():
        global _client, _db
        try:
            if _client:
                _client.close()
        finally:
            _client = None
            _db = None
