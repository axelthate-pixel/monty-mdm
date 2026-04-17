import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mein Tool", page_icon="🛠️", layout="wide")

st.title("🛠️ Mein Citizen Developer Tool")
st.caption("Beschreibe hier kurz, was dein Tool macht.")

# Sample data – replace with your own or load from a file
data = pd.DataFrame([
    {"Name": "Beispiel 1", "Status": "✅ Aktiv", "Kategorie": "A"},
    {"Name": "Beispiel 2", "Status": "⚠️ Offen",  "Kategorie": "B"},
    {"Name": "Beispiel 3", "Status": "🔴 Inaktiv","Kategorie": "A"},
])

# Key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Einträge gesamt", len(data))
col2.metric("Aktiv",   len(data[data["Status"].str.startswith("✅")]))
col3.metric("Inaktiv", len(data[data["Status"].str.startswith("🔴")]))

st.divider()

# Filter
status_filter = st.multiselect(
    "Status filtern",
    options=data["Status"].unique(),
    default=data["Status"].unique(),
)
gefiltert = data[data["Status"].isin(status_filter)]

st.dataframe(gefiltert, use_container_width=True, hide_index=True)

st.divider()
st.info("💡 Tipp: Öffne Copilot Chat (Strg+I) und beschreibe, was du als nächstes hinzufügen möchtest.")
