import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Engenharia Control Center", page_icon="⚡", layout="wide")

st.title("⚡ Dashboard de Engenharia: Faculdade, Estudo & Estágio")
st.markdown("---")

# --- INICIALIZAÇÃO DO ESTADO ---
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Segunda": ["14:00-15:30: Revisão Prediais 🔥", "19:30-21:00: Exercícios Eletrônica 🔥"],
        "Terça": ["10:30-12:00: Revisão Prática Lab 🔥", "19:30-21:00: Lista de Eletrônica"],
        "Quarta": ["14:00-15:30: Dimensionamento / NBR 5410 🔥", "19:30-20:30: Revisão leve"],
        "Quinta": ["19:30-20:30: Revisão rápida de Eletrônica"],
        "Sexta": ["14:00-16:00: Eletrônica Analógica 🔥🔥", "19:00-20:00: Prediais (Cálculo + Norma) 🔥"],
        "Sábado": ["14:30-16:00: Prediais (Exercícios) 🔥", "16:30-17:30: Eletrônica (Simulado)"],
        "Domingo": ["Revisão Geral e Planejamento"]
    }

if 'estagio_info' not in st.session_state:
    st.session_state.estagio_info = "Manhã (08:00 - 12:00)"

# --- BARRA LATERAL (EDIÇÃO E FERRAMENTAS) ---
st.sidebar.header("⚙️ Painel de Controle")

# Editar Estágio
st.sidebar.subheader("💼 Configurar Estágio")
st.session_state.estagio_info = st.sidebar.text_input("Horário do Estágio:", st.session_state.estagio_info)

# Pomodoro Timer
st.sidebar.subheader("⏳ Timer de Estudo (Pomodoro)")
if st.sidebar.button("Iniciar 25 min"):
    st.sidebar.success("Foco total em Eletrônica/Prediais agora!")
    # Nota: Em um app web real, timers complexos exigem javascript, 
    # mas aqui serve como um lembrete visual de foco.

# Notas Rápidas (Dúvidas de Aula)
st.sidebar.subheader("📝 Notas e Dúvidas")
st.sidebar.text_area("Anote aqui para não esquecer:", placeholder="Ex: Dúvida sobre queda de tensão na NBR 5410...")

# --- CORPO DO APP ---
col1, col2 = st.columns([1, 1.2])

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
        st.info(f"**{dia}**: {aula}")

with col2:
    st.header("✅ Checklist de Hoje")
    dia_hoje = st.selectbox("Selecione o dia para focar:", list(st.session_state.estudos.keys()))
    
    # Exibir Estágio se for dia de estágio
    dias_estagio = ["Quinta", "Sexta", "Sábado"]
    if dia_hoje in dias_estagio:
        st.warning(f"💼 **DIA DE ESTÁGIO:** {st.session_state.estagio_info}")
    
    st.write("---")
    st.subheader(f"📚 Missões de Estudo - {dia_hoje}")
    
    # Gerar checkboxes para as tarefas do dia
    for tarefa in st.session_state.estudos[dia_hoje]:
        st.checkbox(tarefa, key=f"{dia_hoje}_{tarefa}")

st.markdown("---")
st.caption("⚡ Foco em Prediais e Eletrônica: O sucesso na Engenharia vem da consistência.")
