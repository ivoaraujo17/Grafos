from grafo import graph
from busca_profundidade import busca_em_profundidade

for i in range(1,21):
    grafo = graph(f"in/graph_{i}")
    busca = busca_em_profundidade(grafo)
    busca.inicializa(1)
