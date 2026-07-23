import streamlit as st
import requests

# Configuração da página da ferramenta interna
st.set_page_config(page_title="Prospecção Industrial - Validação", layout="centered")

st.title("🏭 Prospecção Industrial: Fila de Validação")
st.write("Analise os dados da empresa capturada e decida se ela tem fit comercial antes de enviar para o Salesforce.")

# Exemplo de dados vindos da extração (motor de busca da ferramenta)
lead_atual = {
    "razao_social": "Metalúrgica e Galpões Industriais Ltda",
    "cnpj": "12.345.678/0001-99",
    "endereco": "Rodovia SP-360, Km 45 - Itatiba/SP",
    "segmento": "Galpão Logístico / Alta Demanda de Transformadores",
    "produto_potencial": "Transformadores Trifásicos & Iluminação LED Industrial"
}

# Caixa visual com os dados do lead
with st.container():
    st.info("Novo Prospect Identificado pelo Sistema")
    st.markdown(f"### **{lead_atual['razao_social']}**")
    st.write(f"**CNPJ:** {lead_atual['cnpj']}")
    st.write(f"**Endereço:** {lead_atual['endereco']}")
    st.write(f"**Segmento/Necessidade:** {lead_atual['segmento']}")
    st.write(f"**Portfólio Sugerido:** {lead_atual['produto_potencial']}")

st.divider()

# Função que realiza a integração real com a API do Salesforce
def enviar_para_salesforce(dados):
    # Insira aqui as credenciais e endpoint da sua instância do Salesforce
    instancia = "sua-instancia"
    token = "seu-token-de-acesso"
    
    url = f"https://{instancia}.salesforce.com/services/data/v58.0/sobjects/Account"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "Name": dados["razao_social"],
        "BillingStreet": dados["endereco"],
        "Description": f"Segmento: {dados['segmento']} | Foco: {dados['produto_potencial']}",
        "Rating": "Quente - Aprovado pelo Vendedor"
    }
    
    # Executa o envio
    # response = requests.post(url, json=payload, headers=headers)
    # return response.status_code == 201
    return True # Simulação de sucesso para teste visual

# Botões de decisão do vendedor
col1, col2 = st.columns(2)

with col1:
    if st.button("❌ Descartar (Lead Frio)", use_container_width=True):
        st.warning("Lead descartado. O sistema carregará o próximo da fila.")

with col2:
    if st.button("✅ OK - Enviar para o Salesforce", type="primary", use_container_width=True):
        sucesso = enviar_para_salesforce(lead_atual)
        if sucesso:
            st.success("Lead aprovado e integrado ao Salesforce com sucesso! Conta e tarefa criadas.")
        else:
            st.error("Erro ao integrar com o Salesforce. Verifique as credenciais.")
            
