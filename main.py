import streamlit as st

from views.inicio_view import show_inicio
from views.usuarios_view import show_usuarios


st.set_page_config(
    page_title="Sistema MVC",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


with st.sidebar:
    st.title("🚀 Sistema MVC")

    st.divider()

    pagina = st.radio(
        "Navegação",
        [
            "🏠 Início",
            "👥 Usuários",
            "📖 Livros",
        ]
    )

    st.divider()

    st.caption("Versão 1.0.0")


if pagina == "🏠 Início":
    show_inicio()

elif pagina == "👥 Usuários":
    show_usuarios()
    
elif pagina == "📖 Livros":
    show_usuarios()