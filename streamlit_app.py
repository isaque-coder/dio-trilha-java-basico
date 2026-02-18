import streamlit as st

# Configuração da página
st.set_page_config(page_title="⚡ Meu Cronograma Elétrica", layout="wide")

st.title("⚡ Dashboard de Engenharia: Faculdade, Estudo & Estágio")
st.markdown("---")

# --- INICIALIZAÇÃO DO ESTADO (Para permitir edição) ---
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Segunda": "14:00-15:30: Revisão Prediais | 19:30-21:00: Exercícios Eletrônica",
        "Terça": "10:30-12:00: Revisão Prática Lab | 19:30-21:00: Lista Eletrônica",
        "Quarta": "14:00-15:30: Dimensionamento NBR 5410 | 19:30-20:30: Revisão Leve",
        "Quinta": "19:30-20:30: Revisão Rápida Eletrônica",
        "Sexta": "14:00-16:00: Eletrônica Analógica | 19:00-20:00: Prediais",
        "Sábado": "14:30-16:00: Prediais Exercícios | 16:30-17:30: Simulado",
        "Domingo": "18:00: Revisão Geral e Planejamento"
    }

if 'estagio' not in st.session_state:
    st.session_state.estagio = "08:00 - 12:00 (Quinta, Sexta e Sábado)"

# --- BARRA LATERAL (EDIÇÃO) ---
st.sidebar.header("⚙️ Painel de Controle")
st.sidebar.subheader("Editar Horários de Estágio")
st.session_state.estagio = st.sidebar.text_area("Horário do Estágio:", st.session_state.estagio)

st.sidebar.subheader("Editar Metas de Estudo")
dia_edit = st.sidebar.selectbox("Selecione o dia para editar o estudo:", list(st.session_state.estudos.keys()))
st.session_state.estudos[dia_edit] = st.sidebar.text_area(f"Planos para {dia_edit}:", st.session_state.estudos[dia_edit])

# --- CORPO DO APP ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🏫 Grade Fixa (Faculdade)")
    grade_fixa = {
        "Segunda": "08-12h: Prediais/Potência | 16-18h: Eletrônica",
        "Terça": "08-10h: Conservação | 14-18h: Lab/Sistemas",
        "Quarta": "08-12h: Prediais/Potência | 16-18h: Eletrônica",
        "Quinta": "16:00 - 18:00: Sistemas Lineares",
        "Sexta": "Livre de Aulas",
        "Sábado": "Livre de Aulas"
    }
    for dia, aula in grade_fixa.items():
        st.info(**{dia}**: {aula})

with col2:
    st.header("✅ Checklist de Hoje")
    dia_hoje = st.selectbox("Escolha o dia para focar:", list(st.session_state.estudos.keys()))
    
    st.subheader(f"💼 Estágio: {st.session_state.estagio}")
    
    st.write("---")
    st.subheader(f"📚 Missões de Estudo - {dia_hoje}")
    tarefas = st.session_state.estudos[dia_hoje].split('|')
    
    for tarefa in tarefas:
        st.checkbox(tarefa.strip())

st.markdown("---")
st.caption("Dica: Use a NBR 5410 como livro de cabeceira para Prediais! 💡")
