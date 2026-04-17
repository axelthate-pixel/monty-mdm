import streamlit as st

# Page configuration – adjust title, icon and layout to your use case
st.set_page_config(page_title="Mein Tool", page_icon="🚀", layout="wide")

st.title("🚀 Mein Streamlit-Tool")
st.caption("Beschreibe hier kurz, was dieses Tool macht.")

st.divider()

st.write("Willkommen! Hier entsteht dein Tool.")
st.write(
    "Öffne **Copilot Chat** (`Strg+I` / `Cmd+I`) und beschreibe, "
    "was du hinzufügen möchtest – zum Beispiel eine Tabelle, ein Formular oder ein Diagramm."
)

st.divider()
st.info("💡 Tipp: Öffne `GETTING_STARTED.md` für fertige Copilot-Prompts.")
