import streamlit as st
import time
import random

# Configuração da página
st.set_page_config(page_title="Isaque Maia - Engenharia", page_icon="⚡", layout="wide")

# CSS Customizado para um visual "Tech/Anime"
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .title-isaque { color: #00d4ff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 42px; font-weight: bold; border-bottom: 2px solid #ff8c00; }
    .stCheckbox { background-color: #1e2130; padding: 10px; border-radius: 5px; margin-bottom: 5px; }
    .anime-quote { 
        padding: 15px; border-left: 5px solid #00d4ff; background-color: #262730; 
        font-style: italic; color: #ffffff; margin: 20px 0; border-radius: 0 10px 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# TOPO PERSONALIZADO
st.markdown(f'<div class="title-isaque">ISAQUE MAIA | CRONOGRAMA ⚡</div>', unsafe_allow_html=True)
st.write(f"### Engenharia Elétrica - Foco: Prediais & Eletrônica")

# --- BANCO DE FRASES DE ANIME ---
frases_anime = [
    "⚡ 'Não importa o quão mundano seja o seu trabalho, fazê-lo com todo o seu coração mudará o mundo.' – Rock Lee",
    "⚡ 'Se você não gosta do seu destino, tenha a coragem de mudá-lo.' – Naruto Uzumaki",
    "⚡ 'O impossível não existe para quem tem força de vontade.' – Vegeta",
    "⚡ 'Um mestre falhou mais vezes do que um iniciante sequer tentou.' – Koro-sensei",
    "⚡ 'Pode haver muitas falhas, mas desistir não é uma opção.' – Asta (Black Clover)"
]

# --- FUNÇÃO DE SOM ---
def play_alarm():
    # Som de sino/notificação
    sound_html = '<audio autoplay><source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg"></audio>'
    st.components.v1.html(sound_html, height=0)

# --- INICIALIZAÇÃO DOS DADOS ---
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Segunda": ["Revisão Prediais (NBR 5410) 🔥", "Exercícios de Eletrônica Analógica"],
        "Terça": ["Revisão Prática de Laboratório 🔥", "Lista de Sistemas Lineares"],
        "Quarta": ["Dimensionamento e Cálculos Prediais 🔥", "Revisão Teórica Eletrônica"],
        "Quinta": ["Estudo rápido de Sinais", "Foco em Estágio"],
        "Sexta": ["Eletrônica Analógica (Projeto) 🔥🔥", "Prediais (Cálculo de Carga)"],
        "Sábado": ["Simulado de Eletrônica", "Resumo de Prediais 🔥"],
        "Domingo": ["Organização da Semana"]
    }

# --- LAYOUT ---
col_grade, col_foco = st.columns([1, 1.2])

with col_grade:
    st.markdown("## 🏫 Grade Fixa (Facul)")
    grade = {
        "SEG": "08-12h: Prediais | 16-18h: Eletrônica",
        "TER": "08-10h: Conservação | 14-18h: Lab",
        "QUA": "08-12h: Prediais | 16-18h: Eletrônica",
        "QUI": "16-18h: Sist. Lineares",
        "SEX": "💼 ESTÁGIO (Manhã)",
        "SÁB": "💼 ESTÁGIO (Manhã)"
    }
    for d, a in grade.items():
        st.info(f"**{d}**: {a}")

with col_foco:
    st.markdown("## 🎯 Missões de Hoje")
    dia_selecionado = st.selectbox("Escolha o dia:", list(st.session_state.estudos.keys()))
    
    st.markdown(f'<div class="anime-quote">{random.choice(frases_anime)}</div>', unsafe_allow_html=True)
    
    for tarefa in st.session_state.estudos[dia_selecionado]:
        st.checkbox(tarefa, key=f"task_{dia_selecionado}_{tarefa}")

st.markdown("---")

# --- POMODORO REAL ---
st.markdown("## ⏳ Pomodoro Isaque (Foco Máximo)")
c1, c2 = st.columns([1, 2])

with c1:
    minutos = st.number_input("Minutos de estudo:", value=25)
    if st.button("🚀 INICIAR FOCO"):
        progresso = st.progress(0)
        tempo_total = minutos * 60
        for i in range(tempo_total):
            time.sleep(1)
            progresso.progress((i + 1) / tempo_total)
        st.balloons()
        play_alarm()
        st.success("CICLO COMPLETO! Descanse 5 minutos.")

with c2:
    st.markdown("### 📝 Notas do Dia / Estágio")
    st.text_area("Anote aqui dúvidas ou tarefas do estágio:", height=150, placeholder="Ex: Verificar disjuntores do quadro X...")

# --- SIDEBAR ---
st.sidebar.markdown(f"### ⚡ Engenheiro: \n**Isaque Maia**")
st.sidebar.write("---")
st.sidebar.markdown("### 💼 Horário Estágio")
st.sidebar.text_input("Status:", "08:00 - 12:00 (Ativo)")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3067/3067451.png", width=80)
