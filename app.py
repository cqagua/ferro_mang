import streamlit as st
import pandas as pd
from yaml.loader import SafeLoader
import yaml
import streamlit_authenticator as stauth

st.set_page_config(layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
    
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Criar objeto de autenticação
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Renderizar widget de login
name, authentication_status, username = authenticator.login('Login', 'main')
authenticator.logout('Logout', 'main')

if authentication_status is False:
    st.error('Usuário ou senha incorretos')
elif authentication_status is None:
    st.warning('Por favor, insira seu usuário e senha')
elif authentication_status:   
    dashboard = st.Page(
    "reports/dashboard.py", title="Ferro e Manganês", icon=":material/monitoring:", default=True
    )
    bugs = st.Page("reports/bugs.py", title="Estatística Inferencial", icon=":material/calculate:")


    pg = st.navigation(
        {
            "Análises": [dashboard, bugs]
        }
    )
    pg.run()
else:
    st.warning('Usuário ou senha incorretos')
    st.error('Por favor, tente novamente')