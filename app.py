import streamlit as st
import pandas as pd
from streamlit.runtime.scriptrunner import RerunException
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

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

# 🎯 Choisir le Superset (bloc)
blocs = sorted(df[df["Jour"] == jour_select]["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# 🔍 Filtrer les données
df_bloc = df[(df["Jour"] == jour_select) & (df["Bloc"] == bloc_select)]

# 🏋️‍♂️ Afficher l'exercice
exercice = df_bloc.iloc[0]["Exercice"]
st.markdown(f"### 💥 <span style='color:#000;'>Exercice : <em>{exercice}</em></span>", unsafe_allow_html=True)

# ✅ Cases à cocher
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    value = st.session_state.get(key, False)
    st.session_state[key] = st.checkbox(f"🔥 {row['Series_Reps']}", key=key, value=value)

# 🔄 Réinitialiser le bloc
if st.button("🔁 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        if key in st.session_state:
            del st.session_state[key]
    ctx = get_script_run_ctx()
    if ctx:
        raise RerunException(ctx)




