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

**Markov-Ketten**  
Die bedingte Wahrscheinlichkeit und die Unabhängigkeit von diskreten Ereignissen finden eine wichtige Anwendung in der Modellierung von Markov-Ketten. Eine Markov-Kette beschreibt einen Versuch, bei dem das System verschiedene Zustände durchlaufen kann. Die entscheidende Eigenschaft einer Markov-Kette ist die \textit{Gedächtnislosigkeit}. Diese besagt, dass die Wahrscheinlichkeit für den Übergang in den nächsten Zustand nur vom aktuellen Zustand abhängt und unabhängig ist von der gesamten Vorgeschichte des Systems.  

**Wahrscheinlichkeitsverteilungen**  
Wann immer die Lehre vom Zufall in der Mathematik so verlassen wird, dass sie in der Praxis nicht mehr anwendbar ist, verletzen wir das eigentliche Ziel der Mathematik in diesem wichtigen Thema. Beim Erwartungswert war dies schon der Fall, denn auf die Augenzahl 3,5 wird der Würfel nie zufällig fallen. Damit muss die Lehre vom Zufall in der Mathematik sehr vorsichtig entwickelt werden. Denn wenn man zum Beispiel den Versuch einen Würfel zu würfeln oft wiederholt, ist beobachtbar, dass die Abweichung vom Erwartungswert beachtlich ist.

Die bekannten Wahrscheinlichkeitsverteilungen der Mathematik sind für die unterschiedlichen Versuche mit diskreten Ereignissen mit großer Genauigkeit und Vorsicht anzuwenden. Wird ein Versuch in seiner Beschreibung auf eine Anwendung einer Wahrscheinlichkeitsverteilung überprüft, können kleinste Details in der Beschreibung des Versuchs entscheidend sein für die Wahl der Wahrscheinlichkeitsverteilungen. Wird ein Detail in der Beschreibung des Versuchs übersehen und eine andere Wahrscheinlichkeitsverteilung gewählt, kann dies in der Analyse für den Versuch zu einem anderen Ergebnis führen.

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

<pre>
=========================================================================================================
3-KNF Algorithmus mit Zufall
=========================================================================================================

### EXPERIMENT 1: Variation der Variablenanzahl ###
  Analysiere: 5 Variablen, 20 Klauseln...
  Analysiere: 10 Variablen, 40 Klauseln...
  Analysiere: 15 Variablen, 60 Klauseln...
  Analysiere: 20 Variablen, 80 Klauseln...
  Analysiere: 25 Variablen, 100 Klauseln...

Ergebnisse - Variablenanzahl
=========================================================================================================
Vars   Klauseln  Ø Erfüllt   Std      Theo %     Opt %      Ø Optimal  
=========================================================================================================
5      20        17.64       1.41     100.80   % 88.64%     19.90      
10     40        34.52       1.90     98.63    % 86.56%     39.88      
15     60        52.52       2.53     100.04   % 87.80%     59.82      
20     80        69.46       3.33     99.23    % N/A        N/A        
25     100       87.82       3.50     100.37   % N/A        N/A        
=========================================================================================================

### EXPERIMENT 2: Variation der Klauseldichte ###
  Dichte 2.0: 30 Klauseln...
  Dichte 4.0: 60 Klauseln...
  Dichte 6.0: 90 Klauseln...
  Dichte 8.0: 120 Klauseln...

Ergebnisse - Klauseldichte
=========================================================================================================
Vars   Klauseln  Ø Erfüllt   Std      Theo %     Opt %      Ø Optimal  
=========================================================================================================
15     30        26.32       1.67     100.27   % 87.73%     30.00      
15     60        52.52       2.53     100.04   % 87.80%     59.82      
15     90        78.52       3.04     99.71    % 88.68%     88.54      
15     120       104.68      3.06     99.70    % 89.65%     116.76     
=========================================================================================================

### EXPERIMENT 3: Vergleich mit optimaler Lösung ###
  Analysiere: 4 Variablen, 12 Klauseln...
  Analysiere: 6 Variablen, 18 Klauseln...
  Analysiere: 8 Variablen, 24 Klauseln...
  Analysiere: 10 Variablen, 30 Klauseln...
  Analysiere: 12 Variablen, 36 Klauseln...
  Analysiere: 14 Variablen, 42 Klauseln...

Ergebnisse - Optimaler Vergleich
=========================================================================================================
Vars   Klauseln  Ø Erfüllt   Std      Theo %     Opt %      Ø Optimal  
=========================================================================================================
4      12        10.45       1.50     99.52    % 87.08%     12.00      
6      18        15.85       1.66     100.63   % 88.06%     18.00      
8      24        20.65       1.50     98.33    % 86.04%     24.00      
10     30        25.85       1.57     98.48    % 86.17%     30.00      
12     36        31.30       1.69     99.37    % 86.94%     36.00      
14     42        36.15       2.18     98.37    % 86.07%     42.00      
=========================================================================================================

Grafik als 'experiment-results.svg' gespeichert.
</pre>

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
