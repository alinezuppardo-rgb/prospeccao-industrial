import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="DMP Inteligência - Prospecção Industrial", page_icon="⚡", layout="wide")

# Custom CSS for Econodata professional styling
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #0d6efd; color: white; font-weight: bold; border-radius: 4px; }
    .metric-card { background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ DMP Inteligência — Prospecção B2B (Indústrias & Data Centers)")
st.markdown("Plataforma de inteligência comercial para mapeamento de indústrias, galpões logísticos e data centers.")

# Sidebar Filters (Econodata style)
st.sidebar.header("🔍 Filtros de Busca Avançada")
segmento = st.sidebar.selectbox("Segmento de Mercado", ["Todos", "Indústria de Transformação", "Galpões Logísticos / Armazéns", "Data Centers", "Construção Civil Industrial"])
regiao = st.sidebar.selectbox("Região / Estado", ["Todos", "São Paulo (SP)", "Minas Gerais (MG)", "Paraná (PR)", "Santa Catarina (SC)", "Rio Grande do Sul (RS)"])
porte = st.sidebar.multiselect("Porte da Empresa", ["Microempresa", "Pequena Empresa", "Média Empresa", "Grande Empresa"], default=["Média Empresa", "Grande Empresa"])
status_rf = st.sidebar.selectbox("Situação Cadastral", ["Ativa", "Todas"])

# Mock Database for Demape / Industrial Lighting & Transformers Prospecting
data = [
    {"Empresa": "Indústria Metalúrgica AçoForte S/A", "CNPJ": "12.345.678/0001-90", "Segmento": "Indústria de Transformação", "Cidade/UF": "Campinas / SP", "Porte": "Grande Empresa", "Contato Principal": "Carlos Silva (Eng. Chefe)", "Telefone": "(19) 3456-7890", "Status": "Não Contactado"},
    {"Empresa": "Logística & Armazéns Bandeirantes Ltda", "CNPJ": "98.765.432/0001-12", "Segmento": "Galpões Logísticos / Armazéns", "Cidade/UF": "Jundiaí / SP", "Porte": "Média Empresa", "Contato Principal": "Marcos Vinícius (Manutenção)", "Telefone": "(11) 4589-1234", "Status": "Qualificado"},
    {"Empresa": "HyperScale Data Center Brasil", "CNPJ": "45.123.789/0001-55", "Segmento": "Data Centers", "Cidade/UF": "Barueri / SP", "Porte": "Grande Empresa", "Contato Principal": "Ana Paula Souza (Infraestrutura)", "Telefone": "(11) 5555-8888", "Status": "Proposta Enviada"},
    {"Empresa": "Têxtil Sul Mineira S/A", "CNPJ": "33.222.111/0001-88", "Segmento": "Indústria de Transformação", "Cidade/UF": "Poços de Caldas / MG", "Porte": "Grande Empresa", "Contato Principal": "Roberto Mendes (Diretor Industrial)", "Telefone": "(35) 3721-4321", "Status": "Não Contactado"},
    {"Empresa": "Centro Logístico Rodovia dos Bandeirantes", "CNPJ": "77.888.999/0001-23", "Segmento": "Galpões Logísticos / Armazéns", "Cidade/UF": "Itatiba / SP", "Porte": "Grande Empresa", "Contato Principal": "Juliana Lima (Facilities)", "Telefone": "(11) 4892-9900", "Status": "Não Contactado"}
]

df = pd.DataFrame(data)

# KPI Summary
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><h3>5</h3><p>Empresas Filtradas</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h3>3</h3><p>Grandes Indústrias</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h3>2</h3><p>Data Centers / Galpões</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><h3>Pronto</h3><p>Exportação CRM</p></div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("📋 Lista de Empresas Encontradas")

# Search bar
busca = st.text_input("🔍 Buscar por nome da empresa ou CNPJ:", "")

if busca:
    df = df[df['Empresa'].str.contains(busca, case=False, na=False) | df['CNPJ'].str.contains(busca, case=False, na=False)]

# Display Interactive Table
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")
col_acao1, col_acao2 = st.columns(2)
with col_acao1:
    if st.button("📤 Enviar Selecionados para o Salesforce"):
        st.success("Empresas sincronizadas com sucesso para o pipeline do Salesforce!")
with col_acao2:
    if st.button("📥 Baixar Relatório em Excel (CSV)"):
        st.info("Arquivo gerado pronto para download.")
            
