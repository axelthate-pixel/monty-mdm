# 🚀 Monty MDM – Erste Schritte

Willkommen! Diese Umgebung ist dein Startpunkt für das Monty MDM Tool.  
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

### 📋 Gerät hinzufügen (Formular)
```
Füge der Streamlit-App ein Formular hinzu, mit dem ich ein neues Gerät eintragen kann.
Das Formular soll folgende Felder haben: Gerätename, Modell, OS, Zugewiesen an, Standort.
Nach dem Absenden soll das Gerät in der Tabelle erscheinen.
```

---

### 📊 Diagramm: Geräte pro Standort
```
Füge der App ein Balkendiagramm hinzu, das zeigt wie viele Geräte pro Standort vorhanden sind.
Nutze die eingebauten Streamlit-Chart-Funktionen.
```

---

### 📤 Export als Excel
```
Füge einen Button hinzu, mit dem ich die aktuelle Geräteliste als Excel-Datei herunterladen kann.
Nutze pandas und st.download_button.
```

---

### 🔔 E-Mail-Warnung für Offline-Geräte
```
Erkläre mir, wie ich eine automatische E-Mail-Benachrichtigung einrichten kann,
wenn ein Gerät den Status "Offline" hat. Ich möchte wissen, welche einfachste Lösung
es dafür in Python gibt.
```

---

### 🔗 Echte Daten anbinden
```
Ich möchte die Geräteliste nicht mehr manuell in der app.py pflegen, sondern aus einer
Excel-Datei oder Google Sheet laden. Zeig mir, wie ich das umbaue.
```

---

## Nächste Schritte

Wenn die App so weit ist, dass Marcus sie täglich nutzen kann:

1. **Feedback einholen** – Was fehlt noch? Was ist unklar?
2. **Deployment** – Die App kann kostenlos auf [Streamlit Community Cloud](https://streamlit.io/cloud) deployed werden (kein Azure nötig für den Piloten)
3. **OLA ausfüllen** – Erst dann wird die App zur offiziellen Techem-Plattform-Umgebung

---

*Dieses Template ist Teil der Techem Citizen Developer Plattform.*
