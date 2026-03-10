import streamlit as st

# Variáveis simuladas
protocolo_atual = "000000/0000"
total_paes = 0

st.set_page_config(page_title="Gestão de Protocolo")

st.title("Gestão de Protocolo")

st.write(f"**Protocolo atual:** 1 / **Total:** {total_paes}")

# Protocolo
protocolo = st.text_input(
    "Protocolo",
    value=protocolo_atual,
    disabled=True
)

# Botão copiar
st.code(protocolo)

# Tipo
tipo = st.selectbox(
    "Tipo",
    ["Processo", "Documento"]
)

# Despacho
despacho = st.text_input("Despacho")

# Botões
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Próximo"):
        st.write("➡️ Botão Próximo acionado")

with col2:
    if st.button("Salvar"):
        st.write("💾 Botão Salvar acionado")

with col3:
    if st.button("Encerrar"):
        st.write("Aplicação encerrada")