# HET-Q: Hybrid Enhanced Tracking for Quantum SAT Solving

**Version 1.2**  
**License:** MIT

## Abstract

We present HET-Q, a hybrid quantum-classical framework for structured SAT solving. We demonstrate that solution spaces of random 5-variable SAT instances exhibit small-world network properties (diameter 3, clustering coefficient 0.551). Leveraging this structure, we implement an optimized Grover search circuit requiring only 5 qubits and 34 gates. Our results show measurable quantum acceleration potential with 100-shot simulations on Qiskit Aer.

## Results

| Metric | Value |
|--------|-------|
| Variables | 5 |
| Solutions | 18 |
| Graph nodes | 18 |
| Graph edges | 80 |
| Graph diameter | 3 |
| Clustering coefficient | 0.551 |
| Grover qubits | 5 |
| Grover gates | 34 |
| Circuit depth | 10 |

## Repository Structure

- `quantum/grover_sat.py` - Grover implementation
- `quantum/circuit_metrics.py` - Quantum circuit analysis
- `paper/figures/solution_graph.png` - Solution graph visualization
- `paper/data/graph_metrics.txt` - Graph metrics
- `paper/data/edge_list.txt` - Complete edge list

## Reproduction

```bash
git clone https://github.com/berny52/HET-Q
cd HET-Q
conda env create -f environment.yml
conda activate het-q
python quantum/simulate_grover.py
```

## Citation

```bibtex
@software{hetq2024,
  title = {HET-Q: Hybrid Enhanced Tracking for Quantum SAT Solving},
  author = {Tu Nombre},
  year = {2024},
  url = {https://github.com/berny52/HET-Q}
}
```
