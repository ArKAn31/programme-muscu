import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Programme Muscu Stylé", page_icon="💪", layout="centered")

# Chargement du CSV
df = pd.read_csv("programme_muscu_streamlit.csv")

st.title("💪 Ton Programme Muscu Stylé")

# 🔐 Fonction pour clé unique
def get_key(jour, bloc, serie):
    return f"{jour}_{bloc}_{serie}"

# 🗓️ Sélection du jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# 🎯 Sélection du bloc
df_jour = df[df["Jour"] == jour_select]
blocs = sorted(df_jour["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filtrer le superset
df_bloc = df_jour[df_jour["Bloc"] == bloc_select]
exercice = df_bloc["Exercice"].iloc[0]

st.markdown(f"### 💥 **Exercice : _{exercice}_**")

# ✅ Affichage des séries avec cases à cocher
checkbox_states = []
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    checked = st.checkbox(f"🔥 {row['Series_Reps']} : 10 reps", key=key)
    checkbox_states.append(checked)

# 🔄 Réinitialiser uniquement les clés du bloc courant
if st.button("🔁 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        if key in st.session_state:
            del st.session_state[key]
    st.experimental_rerun()  # fonctionne ici sans import caché

# ✅ Message de succès
if checkbox_states and all(checkbox_states):
    st.success("✅ Superset terminé ! Bien joué champion 🏆")




