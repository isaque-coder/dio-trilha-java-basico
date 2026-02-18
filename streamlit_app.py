import streamlit as st
import time

# Configuração da página e Estilo Customizado (CSS)
st.set_page_config(page_title="Isaque Maia - Engenharia", page_icon="⚡", layout="wide")

# CSS para mudar cores, fontes e esconder o menu padrão da IA
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00d4ff; font-family: 'Courier New', Courier, monospace; font-weight: bold; }
    h2 { color: #ff8c00; }
    .stButton>button { background-color: #00d4ff; color: black; border-radius: 10px; font-weight: bold; }
    .stCheckbox { font-size: 20px; color: #ffffff; }
    .anime-quote { 
        padding: 15px; 
        border-left: 5px solid #ff8c00; 
        background-color: #1e2130; 
        font-style: italic; 
        color: #e0e0e0;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# TÍTULO PERSONALIZADO
st.markdown("<h1>ISAQUE MAIA | CRONOGRAMA ⚡</h1>", unsafe_allow_html=True)
st.subheader("Dashboard de Engenharia Elétrica")

# --- BANCO DE FRASES DE ANIME ---
import random
frases_anime = [
    " 'Se você não gosta do seu destino, não o aceite. Em vez disso, tenha a coragem de mudá-lo.' – Naruto Uzumaki",
    " 'O mundo não é perfeito. Mas ele está lá para nós, fazendo o melhor que pode.' – Roy Mustang (FMA)",
    " 'Pessoas que não podem jogar nada fora, nunca podem esperar mudar nada.' – Armin Arlert (Attack on Titan)",
    " 'Trabalho duro é inútil para aqueles que não acreditam em si mesmos.' – Naruto Uzumaki",
    " 'Não morra pelo seu estágio, viva por ele!' – Adaptado de Portgas D. Ace"
]

# --- FUNÇÃO DE SOM (HTML5) ---
def play_sound():
    sound_html = """
    <audio autoplay>
      <source src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3" type="audio/mpeg">
    </audio>
    """
    st.components.v1.html(sound_html, height=0)

# --- INICIALIZAÇÃO DO ESTADO ---
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Segunda": ["14:00-15:30: NBR 5410 (Prediais) 🔥", "19:30-21:00: Circuitos Eletrônicos 🔥"],
        "Terça": ["10:30-12:00: Relatório de Lab 🔥", "19:30-21:00: Lista de Eletrônica"],
        "Quarta": ["14:00-15:30: Dimensionamento de Cargas 🔥", "19:30-20:30: Revisão Teórica"],
        "Quinta": ["19:30-20:30: Análise de Sinais (Lineares)"],
        "Sexta": ["14:00-16:00: Projeto Eletrônica Analógica 🔥", "19:00-20:00: Normas Técnicas"],
        "Sábado": ["14:30-16:00: Exercícios de Fixação 🔥", "16:30-17:30: Simulado Geral"],
        "Domingo": ["Planejamento da Próxima Semana"]
    }

# --- LAYOUT PRINCIPAL ---
col_grade, col_foco = st.columns([1, 1.2])

with col_grade:
    st.markdown("## 🏫 Grade Fixa")
    # Tabela estilizada
    grade = {
        "SEG": "08-12h: Prediais | 16-18h: Eletrônica",
        "TER": "08-10h: Conservação | 14-18h: Lab",
        "QUA": "08-12h: Prediais | 16-18h: Eletrônica",
        "QUI": "16:00 - 18:00: Sist. Lineares",
        "SEX": "Foco no Estágio (Manhã)",
        "SÁB": "Foco no Estágio (Manhã)"
    }
    for d, a in grade.items():
        st.write(f"**{d}:** {a}")

with col_foco:
    st.markdown("## 🎯 Missões de Hoje")
    dia = st.selectbox("Selecione o dia:", list(st.session_state.estudos.keys()))
    
    # Frase do dia
    st.markdown(f'<div class="anime-quote">{random.choice(frases_anime)}</div>', unsafe_allow_html=True)

    for tarefa in st.session_state.estudos[dia]:
        st.checkbox(tarefa, key=f"chk_{dia}_{tarefa}")

st.markdown("---")

# --- POMODORO TIMER REAL ---
st.markdown("## ⏳ Ciclo de Foco (Pomodoro)")
col_timer, col_info = st.columns([1, 2])

with col_timer:
    tempo_minutos = st.number_input("Duração (min):", value=25)
    if st.button("🚀 INICIAR CICLO"):
        progresso = st.progress(0)
        status_text = st.empty()
        
        for i in range(tempo_minutos * 60):
            time.sleep(1)
            restante = (tempo_minutos * 60) - i
            mins, segs = divmod(restante, 60)
            status_text.text(f"Tempo restante: {mins:02d}:{segs:02d}")
            progresso.progress((i + 1) / (tempo_minutos * 60))
        
        st.balloons()
        st.success("Ciclo Finalizado! Descanse 5 minutos.")
        play_sound() # Toca o som ao acabar

with col_info:
    st.info("💡 Dica de Engenharia: Durante o ciclo de 25 min, foque apenas em um diagrama ou cálculo. Sem celular!")

# --- NOTAS ---
st.sidebar.markdown(f"### 👤 Usuário: {st.user.email if hasattr(st, 'user') else 'Isaque Maia'}")
st.sidebar.markdown("### 💼 Estágio (Editável)")
estagio = st.sidebar.text_area("Notas do Estágio:", "Manhã: 08:00 às 12:00")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/606/606548.png", width=100) # Ícone de Eng. Elétrica
