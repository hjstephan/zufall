"""Experimentelle Analyse des randomisierten 3-SAT Algorithmus."""

import statistics
from typing import List
from dataclasses import dataclass

from pysci.zufall.three_sat import ThreeCNFFormula, RandomizedThreeSAT, brute_force_max_sat

@dataclass
class ExperimentResult:
    """Ergebnis eines einzelnen Experiments."""
    num_vars: int
    num_clauses: int
    avg_satisfied: float
    avg_ratio_to_optimal: float
    avg_ratio_to_theoretical: float
    std_satisfied: float
    min_satisfied: int
    max_satisfied: int
    avg_optimal: float


class ExperimentRunner:
    """Führt systematische Experimente durch."""
    
    def __init__(self, seed: int = 42):
        self.base_seed = seed
    
    def run_single_experiment(self, num_vars: int, num_clauses: int,
                             num_trials: int = 100) -> ExperimentResult:
        """Führt ein Experiment für eine gegebene Konfiguration durch."""
        satisfied_counts = []
        optimal_counts = []
        
        for trial in range(num_trials):
            seed = self.base_seed + trial
            formula = ThreeCNFFormula.generate_random(num_vars, num_clauses, seed=seed)
            
            # Randomisierter Algorithmus
            algo = RandomizedThreeSAT(seed=seed)
            assignment = algo.solve(formula)
            satisfied = assignment.count_satisfied_clauses(formula)
            satisfied_counts.append(satisfied)
            
            # Optimale Lösung (nur für kleine Instanzen)
            if num_vars <= 15:
                optimal, _ = brute_force_max_sat(formula)
                optimal_counts.append(optimal)
        
        # Statistiken
        avg_satisfied = statistics.mean(satisfied_counts)
        std_satisfied = statistics.stdev(satisfied_counts) if len(satisfied_counts) > 1 else 0
        
        theoretical = (7.0 / 8.0) * num_clauses
        avg_ratio_to_theoretical = avg_satisfied / theoretical if theoretical > 0 else 0
        
        if optimal_counts:
            avg_optimal = statistics.mean(optimal_counts)
            avg_ratio_to_optimal = avg_satisfied / avg_optimal if avg_optimal > 0 else 0
        else:
            avg_optimal = float('nan')
            avg_ratio_to_optimal = float('nan')
        
        return ExperimentResult(
            num_vars=num_vars,
            num_clauses=num_clauses,
            avg_satisfied=avg_satisfied,
            avg_ratio_to_optimal=avg_ratio_to_optimal,
            avg_ratio_to_theoretical=avg_ratio_to_theoretical,
            std_satisfied=std_satisfied,
            min_satisfied=min(satisfied_counts),
            max_satisfied=max(satisfied_counts),
            avg_optimal=avg_optimal
        )
    
    def run_variable_analysis(self, var_range: range, 
                             clauses_per_var: float = 4.0,
                             num_trials: int = 100) -> List[ExperimentResult]:
        """Analysiert den Einfluss der Variablenanzahl."""
        results = []
        for num_vars in var_range:
            num_clauses = int(num_vars * clauses_per_var)
            print(f"  Analysiere: {num_vars} Variablen, {num_clauses} Klauseln...")
            result = self.run_single_experiment(num_vars, num_clauses, num_trials)
            results.append(result)
        return results
    
    def run_clause_density_analysis(self, num_vars: int,
                                   density_range: List[float],
                                   num_trials: int = 100) -> List[ExperimentResult]:
        """Analysiert den Einfluss der Klauseldichte."""
        results = []
        for density in density_range:
            num_clauses = int(num_vars * density)
            print(f"  Dichte {density}: {num_clauses} Klauseln...")
            result = self.run_single_experiment(num_vars, num_clauses, num_trials)
            results.append(result)
        return results


def print_results_table(results: List[ExperimentResult], title: str = ""):
    """Gibt eine formatierte Tabelle der Ergebnisse aus."""
    if title:
        print(f"\n{title}")
    print("=" * 105)
    print(f"{'Vars':<6} {'Klauseln':<9} {'Ø Erfüllt':<11} {'Std':<8} "
          f"{'Theo %':<10} {'Opt %':<10} {'Ø Optimal':<11}")
    print("=" * 105)
    
    for r in results:
        opt_str = f"{r.avg_ratio_to_optimal*100:.2f}%" if not (
            isinstance(r.avg_ratio_to_optimal, float) and 
            r.avg_ratio_to_optimal != r.avg_ratio_to_optimal  # NaN check
        ) else "N/A"
        opt_avg_str = f"{r.avg_optimal:.2f}" if not (
            isinstance(r.avg_optimal, float) and 
            r.avg_optimal != r.avg_optimal  # NaN check
        ) else "N/A"
        
        print(f"{r.num_vars:<6} {r.num_clauses:<9} {r.avg_satisfied:<11.2f} "
              f"{r.std_satisfied:<8.2f} {r.avg_ratio_to_theoretical*100:<9.2f}% "
              f"{opt_str:<10} {opt_avg_str:<11}")
    print("=" * 105)