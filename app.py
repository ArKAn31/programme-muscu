import streamlit as st
import pandas as pd

# Chargement du programme
@st.cache_data
def load_data():
    df = pd.read_csv("programme_muscu_streamlit.csv")
    return df

df = load_data()

st.set_page_config(page_title="Programme Muscu", layout="centered")
st.markdown("""
    <style>
    .superset-box {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
    }
    .done-icon {
        font-size: 30px;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏋️ Programme Muscu Complet")

# Sélection du jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("Choisis ton jour :", jours)

# Filtrage des supersets
supersets = sorted(df[df["Jour"] == jour_select]["Superset"].unique())
superset_select = st.selectbox("Choisis le Superset :", supersets)

# Filtrage des lignes concernées
bloc = df[(df["Jour"] == jour_select) & (df["Superset"] == superset_select)].reset_index(drop=True)

# Affichage de la zone d'exercice
st.markdown(f"<div class='superset-box'>", unsafe_allow_html=True)
st.subheader(f"{bloc['Exercice 1'][0]} + {bloc['Exercice 2'][0]}")
st.write("**Séries :**")

checkboxes = []
for i, row in bloc.iterrows():
    label = f"Série {i % 4 + 1}"
    checked = st.checkbox(label, key=f"{jour_select}_{superset_select}_{i}")
    checkboxes.append(checked)

if all(checkboxes):
    st.markdown("<div class='done-icon'>✅ Superset complété !</div>", unsafe_allow_html=True)

# Reset Button
if st.button("Reset les cases ❌"):
    for i in range(len(checkboxes)):
        st.session_state[f"{jour_select}_{superset_select}_{i}"] = False

st.markdown("</div>", unsafe_allow_html=True)

