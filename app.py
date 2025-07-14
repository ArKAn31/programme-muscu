import streamlit as st
import pandas as pd

# Titre
st.markdown("# 💪 Ton Programme Muscu Stylé")

# Lecture du fichier CSV
df = pd.read_csv("programme.csv")

# Sélection du jour et du bloc
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

blocs = sorted(df[df["Jour"] == jour_select]["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filtrage des données pour l'affichage
bloc_data = df[(df["Jour"] == jour_select) & (df["Bloc"] == bloc_select)]
exercice = bloc_data["Exercice"].iloc[0]

st.markdown(f"### 💥 *Exercice* : **_{exercice}_**")

# Affichage des séries avec cases à cocher
all_checked = True
for i, row in bloc_data.iterrows():
    key = f"{jour_select}_{bloc_select}_{row['Series_Reps']}"
    if key not in st.session_state:
        st.session_state[key] = False

    checked = st.checkbox(f"🔥 {row['Series_Reps']}", key=key)
    if not checked:
        all_checked = False

# Affichage de la validation du superset
if all_checked:
    st.success("✅ Superset validé, bien joué champion !")

# Bouton de réinitialisation
if st.button("🔄 Réinitialiser ce bloc"):
    for i, row in bloc_data.iterrows():
        key = f"{jour_select}_{bloc_select}_{row['Series_Reps']}"
        if key in st.session_state:
            st.session_state[key] = False
    st.rerun()





