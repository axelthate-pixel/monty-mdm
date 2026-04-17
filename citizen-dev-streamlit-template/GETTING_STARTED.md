# 🚀 Erste Schritte – Citizen Developer Streamlit Template

Willkommen! Diese Umgebung ist dein Startpunkt für dein eigenes Tool.  
Du brauchst **keine Programmiererfahrung** – GitHub Copilot hilft dir bei jedem Schritt.

---

## App starten

Öffne das **Terminal** (unten in VS Code) und führe diesen Befehl aus:

```bash
streamlit run app.py
```

Die App öffnet sich automatisch im Browser. Fertig.

---

## Copilot Chat öffnen

Drücke `Strg+I` (Windows) oder `Cmd+I` (Mac) – oder klicke auf das Chat-Symbol links.

---

## Fertige Prompts zum Starten

Kopiere einen dieser Prompts in den Copilot Chat und drücke Enter:

---

### 📋 Eigene Tabelle anlegen
```
Passe die Tabelle in app.py an mein Thema an. Mein Tool soll [BESCHREIBUNG] verwalten.
Die Tabelle soll folgende Spalten haben: [SPALTE 1], [SPALTE 2], [SPALTE 3].
Füge passende Beispieldaten ein.
```

---

### ➕ Formular zum Hinzufügen von Einträgen
```
Füge der Streamlit-App ein Formular hinzu, mit dem ich neue Einträge hinzufügen kann.
Das Formular soll die gleichen Felder haben wie die bestehende Tabelle.
Nach dem Absenden soll der Eintrag in der Tabelle erscheinen.
```

---

### 📊 Diagramm hinzufügen
```
Füge der App ein Balkendiagramm hinzu, das die Verteilung nach [SPALTENNAME] zeigt.
Nutze die eingebauten Streamlit-Chart-Funktionen.
```

---

### 📤 Export als Excel
```
Füge einen Button hinzu, mit dem ich die aktuelle Tabelle als Excel-Datei herunterladen kann.
Nutze pandas und st.download_button.
```

---

### 🔗 Daten aus Excel-Datei laden
```
Ich möchte die Daten nicht mehr manuell in app.py pflegen, sondern aus einer
Excel-Datei laden. Zeig mir, wie ich das umbaue.
```

---

### 🔔 Benachrichtigung bei bestimmtem Status
```
Erkläre mir, wie ich eine automatische E-Mail-Benachrichtigung einrichten kann,
wenn ein Eintrag den Status "[STATUS]" hat. Was ist die einfachste Lösung in Python?
```

---

## Nächste Schritte

Wenn dein Tool einsatzbereit ist:

1. **Feedback einholen** – Was fehlt noch? Was ist unklar?
2. **Deployment** – Die App kann kostenlos auf [Streamlit Community Cloud](https://streamlit.io/cloud) deployed werden
3. **OLA ausfüllen** – Erst dann wird die App zur offiziellen Techem-Plattform-Umgebung

---

*Dieses Template ist Teil der Techem Citizen Developer Plattform.*
