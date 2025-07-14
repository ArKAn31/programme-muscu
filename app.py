import streamlit as st
import pandas as pd

# Titre
st.markdown("## 💪 Ton Programme Muscu Stylé")

# Lecture du CSV
df = pd.read_csv("programme.csv")

# Sélection du jour et du superset
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

supersets = sorted(df[df["Jour"] == jour_select]["Bloc"].unique())
superset_select = st.selectbox("🎯 Choisis ton Superset :", supersets)

# Filtrage des données
bloc_data = df[(df["Jour"] == jour_select) & (df["Bloc"] == superset_select)]

# Affichage de l'exercice
exercice_nom = bloc_data["Exercice"].iloc[0]
st.markdown(f"### 💥 *Exercice* : **_{exercice_nom}_**")

# Création des cases à cocher
all_checked = True
for i, row in bloc_data.iterrows():
    key = f"{jour_select}_{superset_select}_{row['Series_Reps']}"
    if key not in st.session_state:
        st.session_state[key] = False

    st.session_state[key] = st.checkbox(f"🔥 {row['Series_Reps']}", key=key)
    if not st.session_state[key]:
        all_checked = False

# ✅ Affichage du logo de validation si toutes les séries sont faites
if all_checked:
    st.success("✅ Superset validé, bien joué champion !")

# 🔄 Bouton de réinitialisation
if st.button("🔄 Réinitialiser ce bloc"):
    for i, row in bloc_data.iterrows():
        key = f"{jour_select}_{superset_select}_{row['Series_Reps']}"
        st.session_state[key] = False
    st.experimental_set_query_params()  # évite les rerun inutiles
    st.warning("🔁 Bloc réinitialisé.")





