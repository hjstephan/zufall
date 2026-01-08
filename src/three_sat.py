"""
Implementierung des randomisierten Algorithmus für 3-SAT.

Dieser Algorithmus erreicht eine Approximationsgüte von 7/8 durch zufällige
Zuweisung von Wahrheitswerten zu Variablen.
"""

import random
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Literal:
    """Repräsentiert ein Literal (Variable mit oder ohne Negation)."""
    var: int
    negated: bool
    
    def __repr__(self):
        return f"{'¬' if self.negated else ''}x{self.var}"


@dataclass
class Clause:
    """Repräsentiert eine Klausel mit genau 3 Literalen."""
    literals: List[Literal]
    
    def __post_init__(self):
        if len(self.literals) != 3:
            raise ValueError("Eine 3-SAT Klausel muss genau 3 Literale haben")
    
    def __repr__(self):
        return f"({' ∨ '.join(str(lit) for lit in self.literals)})"


class ThreeCNFFormula:
    """Repräsentiert eine 3-KNF Formel."""
    
    def __init__(self, num_vars: int, clauses: List[Clause]):
        self.num_vars = num_vars
        self.clauses = clauses
        self.num_clauses = len(clauses)
        
    @classmethod
    def generate_random(cls, num_vars: int, num_clauses: int, 
                       seed: int = None) -> 'ThreeCNFFormula':
        """Generiert eine zufällige 3-KNF Formel."""
        if seed is not None:
            random.seed(seed)
            
        clauses = []
        for _ in range(num_clauses):
            selected_vars = random.sample(range(num_vars), 3)
            literals = [
                Literal(var=var, negated=random.random() < 0.5)
                for var in selected_vars
            ]
            clauses.append(Clause(literals=literals))
            
        return cls(num_vars=num_vars, clauses=clauses)
    
    def __repr__(self):
        return f"3-CNF mit {self.num_vars} Variablen und {self.num_clauses} Klauseln"


class Assignment:
    """Repräsentiert eine Belegung der Variablen mit Wahrheitswerten."""
    
    def __init__(self, values: List[bool]):
        self.values = values
        self.num_vars = len(values)
    
    def evaluate_literal(self, literal: Literal) -> bool:
        """Evaluiert ein Literal unter dieser Belegung."""
        value = self.values[literal.var]
        return not value if literal.negated else value
    
    def evaluate_clause(self, clause: Clause) -> bool:
        """Evaluiert eine Klausel unter dieser Belegung."""
        return any(self.evaluate_literal(lit) for lit in clause.literals)
    
    def count_satisfied_clauses(self, formula: ThreeCNFFormula) -> int:
        """Zählt die Anzahl erfüllter Klauseln."""
        return sum(1 for clause in formula.clauses 
                  if self.evaluate_clause(clause))
    
    def __repr__(self):
        return f"Assignment({[int(v) for v in self.values]})"


class RandomizedThreeSAT:
    """
    Randomisierter Algorithmus für 3-SAT mit 7/8 Approximationsgüte.
    
    Weist jeder Variable unabhängig mit Wahrscheinlichkeit 1/2 den Wert 0 oder 1 zu.
    """
    
    def __init__(self, seed: int = None):
        self.seed = seed
        if seed is not None:
            self._random = random.Random(seed)
    
    def solve(self, formula: ThreeCNFFormula) -> Assignment:
        """Wendet den randomisierten Algorithmus auf die Formel an."""
        values = [self._random.random() < 0.5 for _ in range(formula.num_vars)]
        return Assignment(values)
    
    def theoretical_expected_satisfied(self, formula: ThreeCNFFormula) -> float:
        """Berechnet die theoretisch erwartete Anzahl erfüllter Klauseln (7/8 * m)."""
        return (7.0 / 8.0) * formula.num_clauses


def brute_force_max_sat(formula: ThreeCNFFormula) -> Tuple[int, Assignment]:
    """
    Findet die maximale Anzahl erfüllbarer Klauseln durch vollständige Suche.
    
    WARNUNG: Exponentielle Laufzeit! Nur für kleine Instanzen (≤ 20 Variablen).
    """
    if formula.num_vars > 20:
        raise ValueError("Brute Force nicht praktikabel für > 20 Variablen")
    
    max_satisfied = 0
    best_assignment = None
    
    for i in range(2 ** formula.num_vars):
        values = [(i >> j) & 1 == 1 for j in range(formula.num_vars)]
        assignment = Assignment(values)
        satisfied = assignment.count_satisfied_clauses(formula)
        
        if satisfied > max_satisfied:
            max_satisfied = satisfied
            best_assignment = assignment
    
    return max_satisfied, best_assignment