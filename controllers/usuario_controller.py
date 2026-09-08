from models.usuario_model import UsuarioModel


class UsuarioController:

    ## Bloco responsável por listar e tratar os usuários da base de dados estipulada
    def __init__(self):
        self.model = UsuarioModel()

    def listar_usuarios(self):
        return self.model.listar_todos()

    def buscar_usuario(self, nome):
        if not nome:
            return self.model.listar_todos()

        return self.model.buscar_por_nome(nome)

    def quantidade_usuarios(self):
        usuarios = self.model.listar_todos()

        return len(usuarios)
    
    ## Bloco responsável por cadastrar usuário na base de dados supostamente iria aqui
    
    
    