# Zufall in der Mathematik

Dieses Dokument beschreibt die die Grundlagen für den Zufall in der Mathematik.  

**Einführung in den Zufall**  
In der Mathematik wird zwischen diskreten und kontinuierlichen Ereignissen unterschieden. Diskrete Ereignisse sind "natürliche" Ereignisse, die anschaulich nachvollzogen werden können. Ein klassisches Beispiel ist der sechsseitige Würfel:  
- Jede Seite trägt eine Augenzahl von $1$ bis $6$.  
- Da alle sechs Seiten gleich groß sind, ist keine Seite durch die Beschaffenheit des Würfels bevorzugt.  
- Wenn der Würfel bei einem Wurf auf eine bestimmte Zahl (z. B. die 3) fällt, ist dies ein rein zufälliges Ergebnis und keine Bevorzugung dieser Zahl.  

**Mathematische Grundlagen und Definitionen**  
Um Zufall objektiv zu analysieren, nutzt die Mathematik präzise Definitionen.  
- Versuch: Beschreibt das Vorhaben oder die Handlung, wie zum Beispiel das Werfen eines Würfels.  
- Ereignis: Jedes mögliche Einzelergebnis eines Versuchs (z. B. "der Würfel zeigt eine 2")  
- Ereignisraum $\Omega$: Die Menge aller möglichen Ereignisse, die in einem Versuch eintreten können. Beim Würfeln gilt: $\Omega = \{1, 2, 3, 4, 5, 6\}$.  
- Wahrscheinlichkeit: Das mathematische Verhältnis eines spezifischen Ereignisses zur Gesamtzahl aller möglichen Ereignisse. Da es sechs gleichwertige Seiten gibt, beträgt die Wahrscheinlichkeit für eine bestimmte Zahl genau $\frac{1}{6}$.  

**Mathematische Vollständigkeit**  
Ein Versuch gilt als mathematisch vollständig beschrieben, wenn die Summe der Wahrscheinlichkeiten aller möglichen Ereignisse genau $1$ ergibt. Diese Überprüfung ist die notwendige Grundlage für jede weitere Analyse.  

**Analyse diskreter Ereignisse**  
Ein großer Vorteil diskreter Ereignisse ist, dass sich Wahrscheinlichkeiten oft durch einfaches Abzählen ermitteln lassen. Beispiel: "Nicht die 3 würfeln". Wenn man wissen möchte, wie hoch die Wahrscheinlichkeit ist, dass der Würfel nicht auf die 3 fällt, betrachtet man die alternativen Ereignisse. Der Würfel zeigt eine $1, 2, 4, 5$ oder $6$. Dies sind insgesamt fünf günstige Ereignisse.Daraus ergibt sich eine Wahrscheinlichkeit von $\frac{5}{6}$.  

# 3-KNF Algorithmus mit Zufall

## Projektstruktur

```
zufall/
├── doc/                      # Generierte Dokumentation
├── science/                  # Wissenschaftliche Arbeit
├── src/
│   ├── __init__.py
│   ├── three_sat.py          # 3-SAT
│   └── experiments.py        # Experimente
├── tests/                    # Tests
│   ├── __init__.py
│   ├── test_three_sat.py     # 3-SAT Tests
│   └── test_experiments.py   # Tests für Experimente
├── pytest.ini                # Testbeschreibung für Python
├── requirements.txt
├── run_experiments.py        # Experimente ausführen
└── README.md
```

## Installation

```bash
# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Dependencies installieren
pip install -r requirements.txt
```

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
```

### Experimente ausführen

```bash
python run_experiments.py
```

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

## Analyse der experimentellen Ergebnisse

Die durchgeführten Experimente bestätigen die theoretischen Erwartungen an den Algorithmus mit Zufall für 3-KNF.

**Skalierung mit der Variablenanzahl (Experiment 1)**  
Das erste Experiment untersuchte, wie sich die Anzahl der erfüllten Klauseln bei steigender Problemgröße verhält.  
- Lineares Wachstum: Die Anzahl der erfüllten Klauseln steigt streng linear mit der Anzahl der Variablen $n$ (und somit der Klauseln $m$) an.  
- Theoretische Präzision: Die Spalte Theo % zeigt Werte, die fast ausnahmslos um 99% bis 100% schwanken. Dies belegt, dass der Algorithmus die theoretische Erwartung von $7/8 \cdot m$ (87,5% der Klauseln) in der Praxis exakt trifft.  
- Stabilität: Trotz der Zufallskomponente bleibt die Standardabweichung (Std) verhältnismäßig gering, was auf eine hohe Zuverlässigkeit des Algorithmus bei einzelnen Durchläufen hindeutet.

**Einfluss der Klauseldichte (Experiment 2)**  
Hier wurde die Anzahl der Variablen konstant gehalten ($n=15$), während die Anzahl der Klauseln variiert wurde.  
- Robuste Approximation: Unabhängig davon, ob die Formel "locker" (Dichte 2.0) oder "dicht" (Dichte 8.0) ist, bleibt das Verhältnis zum theoretischen Erwartungswert konstant bei ca. 99,7%.  
- Sättigung des Optimums $O$: Bei geringer Dichte (2.0) ist die Formel oft vollständig erfüllbar ($O = Klauseln$). Mit steigender Dichte nähert sich das Verhältnis zum Optimum der theoretischen Schranke von 87,5% an, da es schwieriger wird, alle Klauseln gleichzeitig zu erfüllen.

**Vergleich mit der optimalen Lösung (Experiment 3)**  
Durch den Einsatz von Brute-Force konnte für Instanzen bis $n=14$ die tatsächliche Approximationsgüte ermittelt werden.  
- Garantie-Check: Der Algorithmus erreicht in allen Testläufen eine Güte von über 86% des Optimums.  
- Effizienz-Trade-off: Während Brute-Force bei $n=14$ bereits spürbare Rechenzeit benötigt ($2^n \cdot m$), liefert der randomisierte Algorithmus in linearer Zeit ($n+m$) eine Lösung, die nur ca. 12-14% unter dem theoretischen Maximum liegt.

**Fazit**: Die Daten belegen, dass der 3-KNF Algorithmus mit Zufall eine hocheffiziente und verlässliche Methode darstellt, um für das 3-KNF Problem eine mathematisch garantierte Lösungsqualität in Sekundenbruchteilen zu liefern.

## Wichtige Erkenntnisse

1. **Theoretische Garantie**: 7/8 ≈ 87.5% aller Klauseln werden im Erwartungswert erfüllt
2. **Experimentelle Bestätigung**: Die Implementierung erreicht ~99-100% der theoretischen Vorhersage
3. **Praktikabilität**: Lineare Laufzeit macht den Algorithmus für große Instanzen nutzbar
4. **Trade-off**: ~87% der optimalen Lösung in linearer Zeit vs. 100% in exponentieller Zeit

## Hinweise

- Brute-Force ist nur für ≤20 Variablen praktikabel
- Für > 15 Variablen wird kein optimaler Vergleich durchgeführt
- Coverage-Reports werden in `doc/htmlcov/` generiert
