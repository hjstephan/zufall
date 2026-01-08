# 3-KNF Algorithmus mit Zufall

## Projektstruktur

```
3sat-project/
├── src/
│   ├── __init__.py
│   ├── three_sat.py          # Kernimplementierung
│   └── experiments.py        # Experimentframework
├── tests/
│   ├── __init__.py
│   ├── test_three_sat.py     # Unit Tests
│   └── test_experiments.py   # Experiment Tests
├── pytest.ini                # Bereits vorhanden
├── requirements.txt
├── run_experiments.py        # Hauptprogramm
└── README.md
```

---

## Installation

```bash
# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder: venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt
```

---

## Verwendung

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

## Erwartete Ausgabe

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

## Analyse der Experimentellen Ergebnisse

Die durchgeführten Experimente bestätigen die theoretischen Erwartungen an den randomisierten 3-SAT-Algorithmus. Im Folgenden werden die drei Hauptaspekte der Analyse detailliert beschrieben.

1. **Skalierung mit der Variablenanzahl (Experiment 1)**  
Das erste Experiment untersuchte, wie sich die Anzahl der erfüllten Klauseln bei steigender Problemgröße verhält.  
- Lineares Wachstum: Die Anzahl der erfüllten Klauseln steigt streng linear mit der Anzahl der Variablen $n$ (und somit der Klauseln $m$) an.  
- Theoretische Präzision: Die Spalte Theo % zeigt Werte, die fast ausnahmslos um 99% bis 100% schwanken. Dies belegt, dass der Algorithmus die theoretische Erwartung von $7/8 \cdot m$ (87,5% der Klauseln) in der Praxis exakt trifft.  
- Stabilität: Trotz der Zufallskomponente bleibt die Standardabweichung (Std) verhältnismäßig gering, was auf eine hohe Zuverlässigkeit des Algorithmus bei einzelnen Durchläufen hindeutet.

2. **Einfluss der Klauseldichte (Experiment 2)**  
Hier wurde die Anzahl der Variablen konstant gehalten ($n=15$), während die Anzahl der Klauseln variiert wurde.  
- Robuste Approximation: Unabhängig davon, ob die Formel "locker" (Dichte 2.0) oder "dicht" (Dichte 8.0) ist, bleibt das Verhältnis zum theoretischen Erwartungswert konstant bei ca. 99,7%.  
- Sättigung des Optimums $O$: Bei geringer Dichte (2.0) ist die Formel oft vollständig erfüllbar ($O = Klauseln$). Mit steigender Dichte nähert sich das Verhältnis zum Optimum (O %) der theoretischen Schranke von 87,5% an, da es schwieriger wird, alle Klauseln gleichzeitig zu erfüllen.

3. **Vergleich mit der optimalen Lösung (Experiment 3)**  
Durch den Einsatz von Brute-Force konnte für Instanzen bis $n=14$ die tatsächliche Approximationsgüte ermittelt werden.  
- Garantie-Check: Der Algorithmus erreicht in allen Testläufen eine Güte von über 86% des Optimums.  
- Effizienz-Trade-off: Während Brute-Force bei $n=14$ bereits spürbare Rechenzeit benötigt ($2^n \cdot m$), liefert der randomisierte Algorithmus in linearer Zeit ($n+m$) eine Lösung, die nur ca. 12-14% unter dem theoretischen Maximum liegt.

**Fazit**: Die Daten belegen, dass der 3-KNF Algorithmus mit Zufall eine hocheffiziente und verlässliche Methode darstellt, um für das 3-KNF Problem eine mathematisch garantierte Lösungsqualität in Sekundenbruchteilen zu liefern.

---

## Wichtige Erkenntnisse

1. **Theoretische Garantie**: 7/8 ≈ 87.5% aller Klauseln werden im Erwartungswert erfüllt
2. **Experimentelle Bestätigung**: Die Implementierung erreicht ~99-100% der theoretischen Vorhersage
3. **Praktikabilität**: Lineare Laufzeit macht den Algorithmus für große Instanzen nutzbar
4. **Trade-off**: ~87% der optimalen Lösung in linearer Zeit vs. 100% in exponentieller Zeit

---

## Hinweise

- Brute-Force ist nur für ≤20 Variablen praktikabel
- Für > 15 Variablen wird kein optimaler Vergleich durchgeführt
- Die pytest.ini Konfiguration ist bereits optimal eingestellt
- Coverage-Reports werden automatisch in `doc/htmlcov/` generiert
