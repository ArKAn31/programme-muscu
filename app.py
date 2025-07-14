import streamlit as st
import pandas as pd
from streamlit.runtime.scriptrunner import RerunException
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

# Configuration de la page
st.set_page_config(page_title="Programme Muscu Stylé", page_icon="💪", layout="centered")

# Chargement des données
df = pd.read_csv("programme_muscu_streamlit.csv")

st.title("💪 Ton Programme Muscu Stylé")

# 🔐 Fonction pour générer une clé unique
def get_key(jour, bloc, serie):
    return f"{jour}_{bloc}_{serie}"

# 🗓️ Choix du jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# 🎯 Choix du bloc / superset
df_jour = df[df["Jour"] == jour_select]
blocs = sorted(df_jour["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filtrer les lignes du bloc sélectionné
df_bloc = df_jour[df_jour["Bloc"] == bloc_select]
exercice = df_bloc["Exercice"].iloc[0]

st.markdown(f"### 💥 **Exercice : _{exercice}_**")

# ✅ Affichage des cases à cocher
checkbox_states = []
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    checked = st.checkbox(f"🔥 {row['Series_Reps']} : 10 reps", key=key)
    checkbox_states.append(checked)

# 🔄 Réinitialisation des cases du bloc
if st.button("🔁 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        if key in st.session_state:
            del st.session_state[key]
    raise RerunException(get_script_run_ctx())

# ✅ Affichage d’un message si tout est coché
if all(checkbox_states):
    st.success("✅ Superset terminé ! Bien joué champion 🏆")




