"""Tests für das Experiment-Framework."""

import pytest
from experiments import ExperimentRunner, ExperimentResult


class TestExperimentRunner:
    def test_runner_initialization(self):
        runner = ExperimentRunner(seed=42)
        assert runner.base_seed == 42
    
    def test_run_single_experiment(self):
        runner = ExperimentRunner(seed=42)
        result = runner.run_single_experiment(num_vars=5, num_clauses=10, num_trials=10)
        
        assert isinstance(result, ExperimentResult)
        assert result.num_vars == 5
        assert result.num_clauses == 10
        assert 0 <= result.avg_satisfied <= 10
    
    def test_run_variable_analysis(self):
        runner = ExperimentRunner(seed=42)
        results = runner.run_variable_analysis(
            var_range=range(5, 11, 5),
            clauses_per_var=3.0,
            num_trials=10
        )
        assert len(results) == 2
        assert results[0].num_vars == 5
    
    def test_approximation_ratio_to_theoretical(self):
        runner = ExperimentRunner(seed=42)
        result = runner.run_single_experiment(num_vars=10, num_clauses=40, num_trials=100)
        assert 0.95 <= result.avg_ratio_to_theoretical <= 1.05


class TestExperimentResult:
    def test_result_creation(self):
        result = ExperimentResult(
            num_vars=10, num_clauses=20, avg_satisfied=17.5,
            avg_ratio_to_optimal=0.875, avg_ratio_to_theoretical=1.0,
            std_satisfied=1.2, min_satisfied=15, max_satisfied=20, avg_optimal=20.0
        )
        assert result.num_vars == 10
        assert result.avg_satisfied == 17.5