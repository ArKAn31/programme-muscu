import streamlit as st
import pandas as pd

# Chargement des données
df = pd.read_csv("programme_muscu_streamlit.csv")

st.set_page_config(page_title="Programme Muscu Stylé", page_icon="💪", layout="centered")

st.title("💪 Ton Programme Muscu Stylé")

# Fonction pour générer une clé unique par case
def get_key(jour, bloc, serie):
    return f"{jour}_{bloc}_{serie}"

# Liste des jours
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# Filtrer les données pour le jour choisi
df_jour = df[df["Jour"] == jour_select]
blocs = sorted(df_jour["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filtrer pour le superset choisi
df_bloc = df_jour[df_jour["Bloc"] == bloc_select]
exercice = df_bloc["Exercice"].iloc[0]

st.markdown(f"### 💥 **Exercice : _{exercice}_**")

# Affichage des séries
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    if key not in st.session_state:
        st.session_state[key] = False

    st.session_state[key] = st.checkbox(f"🔥 {row['Series_Reps']} : 10 reps", key=key, value=st.session_state[key])

# Bouton pour réinitialiser les séries de ce bloc
if st.button("🔄 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        st.session_state[key] = False
    st.experimental_rerun()

# ✅ Affichage d’un logo si toutes les séries du bloc sont cochées
toutes_faites = all(st.session_state[get_key(row["Jour"], row["Bloc"], row["Series_Reps"])] for _, row in df_bloc.iterrows())
if toutes_faites:
    st.success("✅ Superset terminé ! Bien joué !")



