import json
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore


def _carregar_credencial():
    """
    Carrega a credencial do Firebase.

    Prioridade:
    1. Streamlit secrets (deploy/produção)
    2. Arquivo local utils/secrets/key.json (desenvolvimento)
    """
    try:
        import streamlit as st

        if "firebase" in st.secrets:
            dados = dict(st.secrets["firebase"])
            if "private_key" in dados:
                dados["private_key"] = dados["private_key"].replace("\\n", "\n")
            return credentials.Certificate(dados)
    except (FileNotFoundError, KeyError):
        pass

    caminho_chave = Path(__file__).resolve().parent / "secrets" / "key.json"

    if caminho_chave.exists():
        return credentials.Certificate(str(caminho_chave))

    raise RuntimeError(
        "Credenciais do Firebase não encontradas. "
        "Configure [firebase] em .streamlit/secrets.toml "
        "ou adicione utils/secrets/key.json localmente."
    )


def get_firestore_db():
    """Retorna uma instância reutilizável do cliente Cloud Firestore."""
    if not firebase_admin._apps:
        firebase_admin.initialize_app(_carregar_credencial())

    return firestore.client()
