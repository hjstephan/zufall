"""Tests für die 3-SAT Kernimplementierung."""

import pytest
from src.three_sat import (
    Literal, Clause, ThreeCNFFormula, Assignment,
    RandomizedThreeSAT, brute_force_max_sat
)


class TestLiteral:
    def test_literal_creation(self):
        lit = Literal(var=0, negated=False)
        assert lit.var == 0
        assert lit.negated is False
    
    def test_literal_repr(self):
        lit_pos = Literal(var=1, negated=False)
        lit_neg = Literal(var=2, negated=True)
        assert "x1" in str(lit_pos)
        assert "¬" in str(lit_neg)


class TestClause:
    def test_clause_creation(self):
        literals = [Literal(i, False) for i in range(3)]
        clause = Clause(literals=literals)
        assert len(clause.literals) == 3
    
    def test_clause_invalid_size(self):
        with pytest.raises(ValueError):
            Clause(literals=[Literal(0, False)])


class TestThreeCNFFormula:
    def test_formula_creation(self):
        clauses = [Clause([Literal(i, False) for i in range(3)]) for _ in range(5)]
        formula = ThreeCNFFormula(num_vars=3, clauses=clauses)
        assert formula.num_vars == 3
        assert formula.num_clauses == 5
    
    def test_generate_random_formula(self):
        formula = ThreeCNFFormula.generate_random(num_vars=10, num_clauses=20, seed=42)
        assert formula.num_vars == 10
        assert formula.num_clauses == 20
        assert all(len(c.literals) == 3 for c in formula.clauses)
    
    def test_random_formula_reproducibility(self):
        f1 = ThreeCNFFormula.generate_random(10, 20, seed=42)
        f2 = ThreeCNFFormula.generate_random(10, 20, seed=42)
        
        for c1, c2 in zip(f1.clauses, f2.clauses):
            for l1, l2 in zip(c1.literals, c2.literals):
                assert l1.var == l2.var
                assert l1.negated == l2.negated


class TestAssignment:
    def test_assignment_creation(self):
        assignment = Assignment([True, False, True])
        assert assignment.num_vars == 3
    
    def test_evaluate_literal_positive(self):
        assignment = Assignment([True, False])
        assert assignment.evaluate_literal(Literal(0, False)) is True
        assert assignment.evaluate_literal(Literal(1, False)) is False
    
    def test_evaluate_literal_negated(self):
        assignment = Assignment([True, False])
        assert assignment.evaluate_literal(Literal(0, True)) is False
        assert assignment.evaluate_literal(Literal(1, True)) is True
    
    def test_evaluate_clause_satisfied(self):
        assignment = Assignment([True, False, False])
        clause = Clause([Literal(0, False), Literal(1, False), Literal(2, False)])
        assert assignment.evaluate_clause(clause) is True
    
    def test_count_satisfied_clauses(self):
        formula = ThreeCNFFormula.generate_random(5, 10, seed=42)
        assignment = Assignment([True] * 5)
        count = assignment.count_satisfied_clauses(formula)
        assert 0 <= count <= 10


class TestRandomizedThreeSAT:
    def test_algorithm_initialization(self):
        algo = RandomizedThreeSAT(seed=42)
        assert algo.seed == 42
    
    def test_solve_returns_valid_assignment(self):
        formula = ThreeCNFFormula.generate_random(10, 20, seed=42)
        algo = RandomizedThreeSAT(seed=42)
        assignment = algo.solve(formula)
        assert assignment.num_vars == formula.num_vars
    
    def test_solve_reproducibility(self):
        formula = ThreeCNFFormula.generate_random(10, 20, seed=42)
        algo1 = RandomizedThreeSAT(seed=100)
        algo2 = RandomizedThreeSAT(seed=100)
        assert algo1.solve(formula).values == algo2.solve(formula).values
    
    def test_theoretical_expected_satisfied(self):
        formula = ThreeCNFFormula.generate_random(10, 24, seed=42)
        algo = RandomizedThreeSAT()
        assert algo.theoretical_expected_satisfied(formula) == 21.0
    
    def test_approximation_ratio(self):
        """Teste ob die 7/8 Approximation im Durchschnitt erreicht wird."""
        formula = ThreeCNFFormula.generate_random(10, 80, seed=42)
        satisfied_counts = []
        
        for i in range(1000):
            algo = RandomizedThreeSAT(seed=42 + i)
            assignment = algo.solve(formula)
            satisfied_counts.append(assignment.count_satisfied_clauses(formula))
        
        avg_satisfied = sum(satisfied_counts) / len(satisfied_counts)
        theoretical = (7.0 / 8.0) * 80
        assert abs(avg_satisfied - theoretical) < 2.0


class TestBruteForce:
    def test_brute_force_small_instance(self):
        clause = Clause([Literal(i, False) for i in range(3)])
        formula = ThreeCNFFormula(num_vars=3, clauses=[clause])
        max_sat, best_assignment = brute_force_max_sat(formula)
        assert max_sat == 1
    
    def test_brute_force_rejects_large_instance(self):
        formula = ThreeCNFFormula.generate_random(25, 50, seed=42)
        with pytest.raises(ValueError):
            brute_force_max_sat(formula)
    
    def test_brute_force_vs_random_algo(self):
        formula = ThreeCNFFormula.generate_random(8, 20, seed=42)
        max_sat, _ = brute_force_max_sat(formula)
        
        satisfied_counts = []
        for i in range(100):
            algo = RandomizedThreeSAT(seed=42 + i)
            assignment = algo.solve(formula)
            satisfied_counts.append(assignment.count_satisfied_clauses(formula))
        
        avg_satisfied = sum(satisfied_counts) / len(satisfied_counts)
        ratio = avg_satisfied / max_sat
        assert ratio >= 0.80