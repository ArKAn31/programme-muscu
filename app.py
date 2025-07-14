import streamlit as st
import pandas as pd

st.set_page_config(page_title="Programme Muscu Stylé", layout="centered")

# 💪 Titre
st.markdown("<h1 style='text-align: center;'>💪 Ton Programme Muscu Stylé</h1>", unsafe_allow_html=True)

# 📄 Charger les données
df = pd.read_csv("programme_muscu_streamlit.csv")

# 🔑 Créer une clé unique pour chaque série
def get_key(jour, bloc, serie):
    return f"{jour}_{bloc}_{serie}"

# 📅 Choisir le jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# 🎯 Choisir le Superset
blocs = sorted(df[df["Jour"] == jour_select]["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# 🔍 Filtrer les données
df_bloc = df[(df["Jour"] == jour_select) & (df["Bloc"] == bloc_select)]

# 🏋️‍♂️ Afficher l'exercice
exercice = df_bloc.iloc[0]["Exercice"]
st.markdown(f"### 💥 <span style='color:#000;'>Exercice : <em>{exercice}</em></span>", unsafe_allow_html=True)

# ✅ Afficher les séries
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    if key not in st.session_state:
        st.session_state[key] = False
    st.session_state[key] = st.checkbox(f"🔥 {row['Series_Reps']}", key=key, value=st.session_state[key])

# 🔄 Réinitialiser le bloc
if st.button("🔁 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        st.session_state[key] = False
    st.experimental_rerun()





