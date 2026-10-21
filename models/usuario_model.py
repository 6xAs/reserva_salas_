import pandas as pd

from utils.firebase_utils import get_firestore_db


class UsuarioModel:
    COLECAO = "usuarios"
    COLUNAS = ["id", "nome", "email", "perfil", "status"]

    def __init__(self):
        self.db = get_firestore_db()
        self.collection = self.db.collection(self.COLECAO)

    def criar(self, nome, email, perfil, status):
        dados = {
            "nome": nome,
            "email": email,
            "perfil": perfil,
            "status": status,
        }

        documento = self.collection.document()
        documento.set(dados)
        return documento.id

    def listar_todos(self):
        usuarios = []

        for documento in self.collection.stream():
            dados = documento.to_dict()
            usuarios.append({
                "id": documento.id,
                "nome": dados.get("nome", ""),
                "email": dados.get("email", ""),
                "perfil": dados.get("perfil", ""),
                "status": dados.get("status", ""),
            })

        return pd.DataFrame(usuarios, columns=self.COLUNAS)

    def buscar_por_id(self, usuario_id):
        documento = self.collection.document(str(usuario_id)).get()

        if not documento.exists:
            return None

        dados = documento.to_dict()
        return {
            "id": documento.id,
            "nome": dados.get("nome", ""),
            "email": dados.get("email", ""),
            "perfil": dados.get("perfil", ""),
            "status": dados.get("status", ""),
        }

    def buscar_por_nome(self, nome):
        usuarios = self.listar_todos()

        if usuarios.empty:
            return usuarios

        return usuarios[
            usuarios["nome"].str.contains(
                nome, case=False, na=False, regex=False
            )
        ]

    def buscar_por_email(self, email):
        consulta = self.collection.where("email", "==", email).limit(1).stream()

        for documento in consulta:
            dados = documento.to_dict()
            return {
                "id": documento.id,
                "nome": dados.get("nome", ""),
                "email": dados.get("email", ""),
                "perfil": dados.get("perfil", ""),
                "status": dados.get("status", ""),
            }

        return None

    def atualizar(self, usuario_id, nome, email, perfil, status):
        referencia = self.collection.document(str(usuario_id))

        if not referencia.get().exists:
            return False

        referencia.update({
            "nome": nome,
            "email": email,
            "perfil": perfil,
            "status": status,
        })
        return True

    def excluir(self, usuario_id):
        referencia = self.collection.document(str(usuario_id))

        if not referencia.get().exists:
            return False

        referencia.delete()
        return True
