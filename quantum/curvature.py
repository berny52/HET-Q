from GraphRicciCurvature.OllivierRicci import OllivierRicci
import networkx as nx

def compute_curvature(graph):
    orc = OllivierRicci(graph, alpha=0.5)
    orc.compute_ricci_curvature()
    return orc
