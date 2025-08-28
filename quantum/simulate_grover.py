import os
import sys
sys.path.append('.')

def simulate_grover():
    from quantum.grover_sat import GroverSAT
    import pickle
    from qiskit_aer import AerSimulator
    
    with open('grafo_breakthrough.pkl', 'rb') as f:
        G = pickle.load(f)
    
    solutions = list(G.nodes())
    grover = GroverSAT(solutions)
    circuit = grover.create_grover_circuit()
    
    print('SIMULACION GROVER INICIADA...')
    print(f'Configuracion: {grover.n_qubits} qubits, {grover.n_solutions} soluciones')
    
    # Simular
    simulator = AerSimulator()
    compiled_circuit = circuit
    result = simulator.run(compiled_circuit, shots=1000).result()
    counts = result.get_counts()
    
    print('RESULTADOS DE LA SIMULACION:')
    print(f'Shots ejecutados: 1000')
    print(f'Estados unicos medidos: {len(counts)}')
    
    # Mostrar top 10 resultados
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print('Top 10 estados medidos:')
    for state, count in sorted_counts[:10]:
        print(f'{state}: {count} veces')
    
    return counts

if __name__ == "__main__":
    simulate_grover()
