# Copilot Instructions – Techem Citizen Developer Plattform

## Projektkontext
Ich baue die Techem Citizen Developer Plattform. Ziel ist es, Mitarbeitern ohne
Programmiererfahrung zu ermöglichen, eigene Tools mit KI-Unterstützung zu entwickeln.

## Was bisher existiert
Repository "monty-mdm" als funktionierender Pilot:
- Streamlit-App zur Verwaltung von Testhandys (Monty & FSA)
- GitHub Codespaces mit Dev Container (Python 3.12 + Streamlit + Copilot)
- Dependabot für automatische wöchentliche Dependency-Updates
- Auto-Merge Workflow für Patch- und Minor-Updates
- GETTING_STARTED.md mit deutschen Copilot-Prompts für Nicht-Entwickler

## Tech Stack
- Python 3.12
- Streamlit (UI-Framework)
- GitHub Codespaces (Entwicklungsumgebung)
- GitHub Actions (Automatisierung)
- Dependabot (Dependency-Updates)

## Nächste Aufgabe
Erstelle ein generisches Template-Repository "citizen-dev-streamlit-template":
- Keinen Monty-spezifischen Inhalt
- Minimale leere Streamlit-App als Startpunkt
- Identische .devcontainer/ und .github/ Struktur wie monty-mdm
- GETTING_STARTED.md mit generischen deutschen Copilot-Prompts
- README.md mit Anleitung zur Nutzung als GitHub Template Repository

## Arbeitsweise
- Alle Erklärungen und Kommentare auf Deutsch
- Code-Kommentare auf Englisch
- Immer vollständige Dateien liefern, keine Ausschnitte
- Schritt für Schritt vorgehen, auf Bestätigung warten
