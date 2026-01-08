# 3-SAT Randomisierter Algorithmus - Vollständige Python Implementierung

## 📁 Projektstruktur

```
3sat-project/
├── src/
│   ├── __init__.py
│   ├── three_sat.py          # Kernimplementierung
│   └── experiments.py         # Experimentframework
├── tests/
│   ├── __init__.py
│   ├── test_three_sat.py      # Unit Tests
│   └── test_experiments.py    # Experiment Tests
├── pytest.ini                  # Bereits vorhanden
├── requirements.txt
├── run_experiments.py          # Hauptprogramm
└── README.md
```

---

## 📦 Installation

```bash
# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder: venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt
```

---

## 🚀 Verwendung

### Tests ausführen (mit Coverage)

```bash
# Alle Tests mit Coverage
pytest

# Tests mit detailliertem Output
pytest -v

# Nur bestimmte Testdatei
pytest tests/test_three_sat.py

# Coverage-Report im Browser öffnen
# Nach pytest wird HTML-Report in doc/htmlcov/ erstellt
open doc/htmlcov/index.html  # Mac
xdg-open doc/htmlcov/index.html  # Linux
start doc/htmlcov/index.html  # Windows
```

### Experimente ausführen

```bash
python run_experiments.py
```

---

## 📊 Erwartete Ausgabe

```
==================================================================================
3-SAT RANDOMISIERTER ALGORITHMUS - EXPERIMENTELLE ANALYSE
==================================================================================

### EXPERIMENT 1: Variation der Variablenanzahl ###
(Verhältnis Klauseln/Variablen = 4.0, 100 Trials pro Konfiguration)
  Analysiere: 5 Variablen, 20 Klauseln...
  Analysiere: 8 Variablen, 32 Klauseln...
  ...

Ergebnisse - Variable Anzahl
=========================================================================================================
Vars   Klauseln  Ø Erfüllt   Std      Theo %     Opt %      Ø Optimal  
=========================================================================================================
5      20        17.48       1.21     99.91%     87.89%     19.89      
8      32        28.02       1.52     100.07%    87.54%     32.01      
...
```

---

## 🧪 Test Coverage Ziel

- **Ziel**: > 90% Coverage
- **Abgedeckt**:
  - ✅ Alle Kernklassen (Literal, Clause, Formula, Assignment)
  - ✅ Randomisierter Algorithmus
  - ✅ Brute-Force Vergleich
  - ✅ Experiment-Framework
  - ✅ Edge Cases und Fehlerbehandlung

---

## 📈 Wichtige Erkenntnisse

1. **Theoretische Garantie**: 7/8 ≈ 87.5% aller Klauseln werden im Erwartungswert erfüllt
2. **Experimentelle Bestätigung**: Die Implementierung erreicht ~99-100% der theoretischen Vorhersage
3. **Praktikabilität**: Lineare Laufzeit macht den Algorithmus für große Instanzen nutzbar
4. **Trade-off**: ~87% der optimalen Lösung in linearer Zeit vs. 100% in exponentieller Zeit

---

## 📝 Hinweise

- Brute-Force ist nur für ≤20 Variablen praktikabel
- Für > 15 Variablen wird kein optimaler Vergleich durchgeführt
- Die pytest.ini Konfiguration ist bereits optimal eingestellt
- Coverage-Reports werden automatisch in `doc/htmlcov/` generiert
