import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Programme Muscu Stylé", layout="centered")

# Titre principal
st.markdown("<h1 style='text-align: center;'>💪 Ton Programme Muscu Stylé</h1>", unsafe_allow_html=True)

# Charger le fichier CSV
df = pd.read_csv("programme_muscu_streamlit.csv")

# Créer une clé unique pour chaque case à cocher
def get_key(jour, bloc, serie):
    return f"{jour}_{bloc}_{serie}"

# Sélection du jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# Sélection du bloc / superset
blocs = sorted(df[df["Jour"] == jour_select]["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filtrer le dataframe pour ce bloc
df_bloc = df[(df["Jour"] == jour_select) & (df["Bloc"] == bloc_select)]

# Afficher l'exercice correspondant
exercice = df_bloc.iloc[0]["Exercice"]
st.markdown(f"### 💥 <span style='color:#000;'>Exercice : <em>{exercice}</em></span>", unsafe_allow_html=True)

# Afficher les séries avec des cases à cocher
for i, row in df_bloc.iterrows():
    key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
    if key not in st.session_state:
        st.session_state[key] = False
    st.checkbox(f"🔥 {row['Series_Reps']}", key=key)

# Bouton pour reset uniquement ce bloc
if st.button("🔁 Réinitialiser ce bloc"):
    for i, row in df_bloc.iterrows():
        key = get_key(row["Jour"], row["Bloc"], row["Series_Reps"])
        if key in st.session_state:
            del st.session_state[key]
    st.experimental_rerun()





