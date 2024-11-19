import streamlit as st
# Configuração da página



st.set_page_config(page_title="Cadastro de Paciente - Saúde")

# Título da página
st.title("Cadastro de Paciente")
st.markdown("Por favor, preencha os dados abaixo para o seu cadastro.")

# Formulário de cadastro
with st.form("cadastro"):
    # Informações pessoais
    st.header("Informações Pessoais")
    nome = st.text_input("Nome completo", placeholder="Digite seu nome completo")
    data_nascimento = st.date_input("Data de nascimento")
    sexo = st.radio("Sexo", ["Masculino", "Feminino", "Outro"])

    # Contato
    st.header("Informações de Contato")
    email = st.text_input("E-mail", placeholder="exemplo@vitally.com")
    senha = st.text_input("Senha", placeholder="Crie uma senha (min 8 dígitos)", type = 'password')
    telefone = st.text_input("Telefone", placeholder="(XX) XXXXX-XXXX")
    
    enviado = st.form_submit_button("Continue")
    

# Exibe mensagem após envio do formulário
if enviado:
    if nome and email and telefone and senha and len(senha) >= 8:
        st.switch_page("pages/Informações Pessoais.py")
    elif nome and email and telefone and senha and len(senha) < 8:
        st.error("A senha deve ter no mínimo 8 caracteres.")
    else:
        st.error("Por favor, preencha todos os campos obrigatórios.")    


        
