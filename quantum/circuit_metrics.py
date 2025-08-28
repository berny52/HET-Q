import os
import sys
sys.path.append('.')

def analyze_grover_circuit():
    from quantum.grover_sat import GroverSAT
    import pickle
    
    with open('grafo_breakthrough.pkl', 'rb') as f:
        G = pickle.load(f)
    
    solutions = list(G.nodes())
    grover = GroverSAT(solutions)
    circuit = grover.create_grover_circuit()
    
    print('METRICAS DEL CIRCUITO GROVER')
    print(f'Qubits: {circuit.num_qubits}')
    print(f'Puertas: {circuit.size()}')
    print(f'Profundidad: {circuit.depth()}')
    print(f'Soluciones: {len(solutions)}')
    
    return circuit

if __name__ == "__main__":
    analyze_grover_circuit()
