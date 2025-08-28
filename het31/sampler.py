import numpy as np
from pysat.formula import CNF

def sample_solutions(cnf_path, n_samples=500, steps=50):
    cnf = CNF(from_file=cnf_path)
    clauses = cnf.clauses
    n = cnf.nv
    total = len(clauses)
    solutions = []
    for _ in range(n_samples):
        a = np.random.randint(0, 2, n)
        for _ in range(steps):
            unsat = [c for c in clauses
                     if not any((lit > 0) == a[abs(lit) - 1] for lit in c)]
            if not unsat:
                break
            c = unsat[np.random.randint(len(unsat))]
            v = abs(c[np.random.randint(len(c))]) - 1
            a[v] ^= 1
        sat_ratio = sum(any((lit > 0) == a[abs(lit) - 1] for lit in c) for c in clauses) / total
        solutions.append((tuple(a), sat_ratio))
    return solutions
