import re

from models.usuario_model import UsuarioModel


class UsuarioController:
    PERFIS_PERMITIDOS = ["Administrador", "Professor", "Usuário"]
    STATUS_PERMITIDOS = ["Ativo", "Inativo"]

    def __init__(self):
        self.model = UsuarioModel()

    def listar_usuarios(self):
        return self.model.listar_todos()

    def buscar_usuario(self, nome):
        if not nome:
            return self.model.listar_todos()

        return self.model.buscar_por_nome(nome.strip())

    def quantidade_usuarios(self):
        return len(self.model.listar_todos())

    def cadastrar_usuario(self, nome, email, perfil, status):
        nome = (nome or "").strip()
        email = (email or "").strip().lower()

        if not nome:
            return False, "Informe o nome do usuário."

        if not email:
            return False, "Informe o e-mail do usuário."

        if not self._email_valido(email):
            return False, "Informe um e-mail válido."

        if perfil not in self.PERFIS_PERMITIDOS:
            return False, "Selecione um perfil válido."

        if status not in self.STATUS_PERMITIDOS:
            return False, "Selecione um status válido."

        if self.model.buscar_por_email(email):
            return False, "Já existe um usuário cadastrado com este e-mail."

        usuario_id = self.model.criar(nome, email, perfil, status)

        return True, usuario_id

    @staticmethod
    def _email_valido(email):
        padrao = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        return re.match(padrao, email) is not None
