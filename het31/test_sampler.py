from het31.sampler import sample_solutions
from pysat.formula import CNF

def test_sampler_runs():
    cnf = CNF()
    cnf.append([1, 2])
    cnf.append([-1, 2])
    cnf.to_file("temp.cnf")          # crea CNF temporal
    solutions = sample_solutions("temp.cnf", n_samples=10, steps=5)
    assert len(solutions) == 10
    import os; os.remove("temp.cnf") # limpia
