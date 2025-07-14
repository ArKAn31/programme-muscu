
import streamlit as st
import pandas as pd

# Load workout program
df = pd.read_csv("programme_muscu_streamlit.csv")

st.set_page_config(page_title="Programme Muscu Pro", layout="centered")

# Custom CSS for cleaner, modern look
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .superset {
        margin-top: 1.5rem;
        padding: 1rem;
        border-left: 5px solid #4CAF50;
        background-color: #f9f9f9;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💪 Programme Muscu Pro")

# Sidebar navigation
jours = df["Jour"].unique()
jour_selectionne = st.sidebar.radio("📅 Sélectionne un jour", jours)

# Filter by selected day
jour_df = df[df["Jour"] == jour_selectionne]

st.markdown(f"## {jour_selectionne}")

# Button reset
if st.button("♻️ Reset cette séance"):
    st.session_state.clear()

# Display Supersets
for i, row in jour_df.iterrows():
    with st.container():
        st.markdown(f"<div class='superset'><strong>{row['Bloc']}</strong><br>{row['Exercice']}<br><em>{row['Series_Reps']}</em></div>", unsafe_allow_html=True)
        # Checkbox
        key = f"check_{i}"
        st.checkbox("✅ Fait", key=key)

# Suggestions en bas pour améliorer l'entraînement
if jour_selectionne == "Jour 4":
    st.markdown("### 🔧 Suggestions d'amélioration pour cette séance :")
    st.markdown("""
    - Réorganiser les biceps avant les triceps (point faible)
    - Réduire les doublons dans les curls
    - Laisser un bloc libre type **Avant-bras / Abdos**
    """)

st.markdown("---")
st.caption("Made with ❤️ pour ton projet pro")
