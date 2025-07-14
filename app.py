import streamlit as st
import pandas as pd

st.set_page_config(layout="centered", page_title="Programme Muscu", page_icon="💪")

# Load data
df = pd.read_csv("programme_muscu_streamlit.csv")

# Checkbox state
if "checked" not in st.session_state:
    st.session_state.checked = {}

st.title("🏋️‍♂️ Ton Programme Muscu Stylé")

# Selection jour
jours = sorted(df["Jour"].unique())
jour_select = st.selectbox("📅 Sélectionne ton jour :", jours)

# Filter by selected jour
df_jour = df[df["Jour"] == jour_select]

# Selection bloc
blocs = sorted(df_jour["Bloc"].unique())
bloc_select = st.selectbox("🎯 Choisis ton Superset :", blocs)

# Filter by bloc
df_bloc = df_jour[df_jour["Bloc"] == bloc_select]

# Get exercice name
exercice = df_bloc["Exercice"].iloc[0]
st.markdown(f"### 💥 Exercice : *{exercice}*")

# Affiche les séries avec checkbox
series = df_bloc["Series_Reps"].tolist()
all_done = True
for serie in series:
    key = f"{jour_select}-{bloc_select}-{serie}"
    if key not in st.session_state.checked:
        st.session_state.checked[key] = False

    st.session_state.checked[key] = st.checkbox(f"✅ {serie}", key=key, value=st.session_state.checked[key])
    if not st.session_state.checked[key]:
        all_done = False

# Logo validé si tout est coché
if all_done:
    st.success("✅ Superset complété !")
    st.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=100)

# Bouton pour reset le bloc
if st.button("🔄 Réinitialiser ce bloc"):
    for serie in series:
        key = f"{jour_select}-{bloc_select}-{serie}"
        st.session_state.checked[key] = False
    st.rerun()


