
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Programme Muscu", page_icon="💪")

st.title("💪 Programme Muscu – Suivi par Jour")
st.markdown("Utilise les cases à cocher pour suivre ta progression. Appuie sur **Reset** pour recommencer une séance.")

@st.cache_data
def load_data():
    return pd.read_csv("programme_muscu_streamlit.csv")

df_original = load_data()

days = df_original["Jour"].unique()
selected_day = st.sidebar.selectbox("📅 Choisis ton jour d'entraînement", days)

df_day = df_original[df_original["Jour"] == selected_day]

if "checked" not in st.session_state:
    st.session_state.checked = {}

if st.button("♻️ Reset la séance"):
    st.session_state.checked = {}

for superset in df_day["Superset"].unique():
    st.subheader(superset)
    block = df_day[df_day["Superset"] == superset]
    cols = st.columns(4)
    for idx, row in block.iterrows():
        key = f"{row['Jour']}_{row['Superset']}_{row['Série']}"
        checked = st.session_state.checked.get(key, False)
        st.session_state.checked[key] = cols[idx % 4].checkbox(
            f"{row['Exercice 1']} / {row['Exercice 2']} – {row['Série']}",
            value=checked,
            key=key
        )
