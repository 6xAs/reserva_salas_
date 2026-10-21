import streamlit as st

from controllers.usuario_controller import UsuarioController


def show_usuarios():
    controller = UsuarioController()

    st.title("👥 Usuários")
    st.write("Cadastro e consulta dos usuários do sistema.")

    tab_cadastro, tab_consulta = st.tabs(["➕ Cadastrar", "🔎 Consultar"])

    with tab_cadastro:
        st.subheader("Novo usuário")

        with st.form("form_cadastrar_usuario", clear_on_submit=True):
            nome = st.text_input("Nome *", placeholder="Digite o nome completo")
            email = st.text_input("E-mail *", placeholder="nome@exemplo.com")

            col_perfil, col_status = st.columns(2)

            with col_perfil:
                perfil = st.selectbox(
                    "Perfil *",
                    controller.PERFIS_PERMITIDOS,
                )

            with col_status:
                status = st.selectbox(
                    "Status *",
                    controller.STATUS_PERMITIDOS,
                )

            cadastrar = st.form_submit_button(
                "Cadastrar usuário",
                use_container_width=True,
                type="primary",
            )

        if cadastrar:
            sucesso, resultado = controller.cadastrar_usuario(
                nome,
                email,
                perfil,
                status,
            )

            if sucesso:
                st.success(
                    f"Usuário cadastrado com sucesso. ID: {resultado}"
                )
            else:
                st.error(resultado)

    with tab_consulta:
        nome_pesquisa = st.text_input(
            "Pesquisar usuário",
            placeholder="Digite um nome...",
            key="pesquisa_usuario",
        )

        usuarios = controller.buscar_usuario(nome_pesquisa)

        st.subheader("Usuários encontrados")

        st.dataframe(
            usuarios,
            use_container_width=True,
            hide_index=True,
        )

        st.caption(
            f"{len(usuarios)} usuário(s) encontrado(s)."
        )
