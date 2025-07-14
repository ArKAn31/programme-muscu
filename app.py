import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Programme Muscu Pro", layout="centered")

# Charger le fichier CSV
df = pd.read_csv("programme_muscu_streamlit.csv")

# Titre principal
st.title("💪 Programme Muscu Pro")

# Sidebar avec navigation entre les jours
jours = df["Jour"].unique()
jour_selectionne = st.sidebar.radio("📅 Choisis ta séance :", jours)

# Bouton de reset des cases cochées pour la séance en cours
if st.button("♻️ Réinitialiser cette séance"):
    for key in st.session_state.keys():
        st.session_state[key] = False

# Filtrer les blocs du jour sélectionné
jour_df = df[df["Jour"] == jour_selectionne]

# Affichage de la séance sélectionnée
st.header(jour_selectionne)

# Boucle sur les supersets
for i, row in jour_df.iterrows():
    bloc = row["Bloc"]
    exercice = row["Exercice"]
    series = row["Series_Reps"]
    checkbox_id = f"{jour_selectionne}_{i}"

    with st.expander(f"✅ {bloc}"):
        st.write(f"**Exercice :** {exercice}")
        st.write(f"**Séries/Répétitions :** {series}")
        st.checkbox("Marquer comme terminé", key=checkbox_id)

# Suggestions spécifiques séance bras
if jour_selectionne.lower() == "jour 4":
    st.markdown("---")
    st.subheader("🔧 Suggestions séance bras")
    st.markdown(
        """
        - Mettre les biceps avant les triceps (point faible)
        - Alléger les curls trop proches (marteau + barre droite)
        - Dernier superset → écrire juste « Avant-bras / Abdos (libre) »
        """
    )

# Pied de page
st.markdown("---")
st.caption("🛠️ Fait avec Streamlit pour booster tes séances !")
