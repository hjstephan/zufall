"""Hauptprogramm für experimentelle Analyse mit Plotting."""

import matplotlib.pyplot as plt
from .experiments import ExperimentRunner, print_results_table

def plot_results(results_vars):
    """Erstellt eine SVG-Grafik der Ergebnisse."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot: Variablenanzahl vs. Erfüllte Klauseln
    vars_x = [r.num_vars for r in results_vars]
    satisfied_y = [r.avg_satisfied for r in results_vars]
    theoretical_y = [(7/8) * r.num_clauses for r in results_vars]
    optimal_y = [r.avg_optimal for r in results_vars]
    
    ax.plot(vars_x, optimal_y, 's-', label='Optimum (tatsächlich erfüllbar)', linewidth=2, color='green')
    ax.plot(vars_x, satisfied_y, 'o-', label='Experimentell (Ø)', linewidth=2)
    ax.plot(vars_x, theoretical_y, 'r--', label='Theoretisch (7/8 m)', linewidth=2)
    ax.set_xlabel('Anzahl Variablen')
    ax.set_ylabel('Erfüllte Klauseln')
    ax.set_title('Skalierung mit Variablenanzahl')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.savefig("experiment-results.svg", format='svg')
    print("\nGrafik als 'experiment-results.svg' gespeichert.")

def main():
    print("=" * 105)
    print("3-KNF Algorithmus mit Zufall")
    print("=" * 105)
    
    runner = ExperimentRunner(seed=42)
    
    # Experiment 1: Schnellere Konfiguration
    print("\n### EXPERIMENT 1: Variation der Variablenanzahl ###")
    results_vars = runner.run_variable_analysis(
        var_range=range(5, 26, 5), # 5, 10, 15, 20, 25
        clauses_per_var=4.0,
        num_trials=50 # Reduziert für Speed
    )
    print_results_table(results_vars, "Ergebnisse - Variablenanzahl")
    
    # Experiment 2: Variation der Klauseldichte
    print("\n### EXPERIMENT 2: Variation der Klauseldichte ###")
    densities = [2.0, 4.0, 6.0, 8.0]
    results_density = runner.run_clause_density_analysis(
        num_vars=15,
        density_range=densities,
        num_trials=50
    )
    print_results_table(results_density, "Ergebnisse - Klauseldichte")
    
    # Experiment 3: Vergleich mit optimaler Lösung (Kritisch für Laufzeit)
    print("\n### EXPERIMENT 3: Vergleich mit optimaler Lösung ###")
    results_optimal = runner.run_variable_analysis(
        var_range=range(4, 15, 2), # Max 14 Variablen für < 1min Laufzeit
        clauses_per_var=3.0,
        num_trials=20 # Deutlich reduziert wegen Brute-Force
    )
    print_results_table(results_optimal, "Ergebnisse - Optimaler Vergleich")
    
    # Visualisierung (nur Plot 1)
    plot_results(results_vars)

if __name__ == "__main__":
    main()