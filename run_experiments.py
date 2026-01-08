"""Hauptprogramm für experimentelle Analyse mit Plotting."""

import matplotlib.pyplot as plt
from experiments import ExperimentRunner, print_results_table

def plot_results(results_vars, results_density):
    """Erstellt eine SVG-Grafik der Ergebnisse."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1: Variablenanzahl vs. Erfüllte Klauseln
    vars_x = [r.num_vars for r in results_vars]
    satisfied_y = [r.avg_satisfied for r in results_vars]
    theoretical_y = [(7/8) * r.num_clauses for r in results_vars]
    
    ax1.plot(vars_x, satisfied_y, 'o-', label='Experimentell (Ø)')
    ax1.plot(vars_x, theoretical_y, 'r--', label='Theoretisch (7/8 m)')
    ax1.set_xlabel('Anzahl Variablen')
    ax1.set_ylabel('Erfüllte Klauseln')
    ax1.set_title('Skalierung mit Variablenanzahl')
    ax1.legend()
    ax1.grid(True)

    # Plot 2: Klauseldichte vs. Approximationsratio
    densities_x = [r.num_clauses / r.num_vars for r in results_density]
    ratio_y = [r.avg_ratio_to_theoretical * 100 for r in results_density]
    
    ax2.plot(densities_x, ratio_y, 's-', color='green', label='Ratio zur Theorie')
    ax2.axhline(y=100, color='red', linestyle='--', label='100% Erwartungswert')
    ax2.set_xlabel('Klauseldichte (m/n)')
    ax2.set_ylabel('Ratio zum theoretischen Erwartungswert (%)')
    ax2.set_title('Einfluss der Klauseldichte')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("experiment_results.svg", format='svg')
    print("\nGrafik als 'experiment_results.svg' gespeichert.")

def main():
    print("=" * 90)
    print("3-SAT RANDOMISIERTER ALGORITHMUS - SCHNELLE ANALYSE")
    print("=" * 90)
    
    runner = ExperimentRunner(seed=42)
    
    # Experiment 1: Schnellere Konfiguration
    print("\n### EXPERIMENT 1: Variation der Variablenanzahl ###")
    results_vars = runner.run_variable_analysis(
        var_range=range(5, 26, 5), # 5, 10, 15, 20, 25
        clauses_per_var=4.0,
        num_trials=50 # Reduziert für Speed
    )
    print_results_table(results_vars, "Ergebnisse - Variable Anzahl")
    
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
    
    # Visualisierung
    plot_results(results_vars, results_density)

if __name__ == "__main__":
    main()