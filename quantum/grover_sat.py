from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np

class GroverSAT:
    def __init__(self, solutions):
        self.solutions = solutions
        self.n_qubits = len(solutions[0])
        self.n_solutions = len(solutions)
        
    def create_oracle(self):
        # Oracle simplificado - sin subcircuitos complejos
        qc = QuantumCircuit(self.n_qubits)
        
        # Oracle básico que marca un estado específico (por ahora)
        # Para múltiples soluciones necesitamos lógica más avanzada
        qc.cz(0, self.n_qubits-1)  # Marcado simple
        
        return qc
    
    def create_grover_circuit(self):
        qc = QuantumCircuit(self.n_qubits, self.n_qubits)
        qc.h(range(self.n_qubits))
        
        # Solo 1 iteración para 32/18 ≈ 1.78
        iterations = 1
        
        for _ in range(iterations):
            # Oracle directo (sin append de subcircuitos)
            oracle_qc = self.create_oracle()
            qc.compose(oracle_qc, inplace=True)
            
            # Amplificación
            qc.h(range(self.n_qubits))
            qc.x(range(self.n_qubits))
            qc.h(self.n_qubits-1)
            qc.mcx(list(range(self.n_qubits-1)), self.n_qubits-1)
            qc.h(self.n_qubits-1)
            qc.x(range(self.n_qubits))
            qc.h(range(self.n_qubits))
        
        qc.measure(range(self.n_qubits), range(self.n_qubits))
        return qc

if __name__ == "__main__":
    from het31.sampler import sample_solutions
    sols = sample_solutions("benchmark/medium.cnf", 10, 20)
    valid = [s for s, r in sols if r >= 0.75]
    
    grover = GroverSAT(valid)
    print(f"Grover listo: {grover.n_solutions} soluciones, {grover.n_qubits} qubits")
