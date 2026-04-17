import streamlit as st
import pandas as pd

st.set_page_config(page_title="Monty MDM", page_icon="📱", layout="wide")

st.title("📱 Monty MDM – Testhandy-Verwaltung")
st.caption("Mobile Device Management für Monty & FSA Testhandys")

# Beispieldaten – von Copilot erweiterbar
devices = pd.DataFrame([
    {"Gerätename": "Monty-iPhone-01", "Modell": "iPhone 14",  "OS": "iOS 17.4",    "Status": "✅ Aktiv",     "Zugewiesen an": "Max Müller",    "Standort": "Hamburg"},
    {"Gerätename": "Monty-Samsung-02","Modell": "Galaxy S23", "OS": "Android 14",  "Status": "✅ Aktiv",     "Zugewiesen an": "Jana Koch",     "Standort": "Berlin"},
    {"Gerätename": "FSA-iPhone-03",   "Modell": "iPhone 13",  "OS": "iOS 16.7",    "Status": "⚠️ Update",   "Zugewiesen an": "Nicht vergeben","Standort": "Frankfurt"},
    {"Gerätename": "FSA-Pixel-04",    "Modell": "Pixel 7",    "OS": "Android 13",  "Status": "🔴 Offline",   "Zugewiesen an": "Tom Weber",     "Standort": "München"},
    {"Gerätename": "Monty-iPad-05",   "Modell": "iPad Air 5", "OS": "iPadOS 17.2", "Status": "✅ Aktiv",     "Zugewiesen an": "Sara Bauer",    "Standort": "Hamburg"},
])

# Kennzahlen oben
col1, col2, col3, col4 = st.columns(4)
col1.metric("Geräte gesamt", len(devices))
col2.metric("Aktiv", len(devices[devices["Status"].str.startswith("✅")]))
col3.metric("Brauchen Update", len(devices[devices["Status"].str.startswith("⚠️")]))
col4.metric("Offline", len(devices[devices["Status"].str.startswith("🔴")]))

st.divider()

# Filter
col_f1, col_f2 = st.columns(2)
with col_f1:
    status_filter = st.multiselect(
        "Status filtern",
        options=devices["Status"].unique(),
        default=devices["Status"].unique()
    )
with col_f2:
    standort_filter = st.multiselect(
        "Standort filtern",
        options=devices["Standort"].unique(),
        default=devices["Standort"].unique()
    )

gefiltert = devices[
    devices["Status"].isin(status_filter) &
    devices["Standort"].isin(standort_filter)
]

st.dataframe(gefiltert, use_container_width=True, hide_index=True)

st.divider()
st.info("💡 Tipp: Öffne Copilot Chat (Strg+I) und beschreibe, was du als nächstes hinzufügen möchtest.")
