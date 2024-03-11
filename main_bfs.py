from grafo import graph
from busca_largura import busca_em_largura

for i in range(1,21):
    grafo = graph(f"in/graph_{i}")
    busca = busca_em_largura(grafo)
    busca.inicializa(1)
    print("--------------------------------")
    print("Excentricidade do vertice 1: ", busca.excentricidade)
    print("metricas do grafo: ", i)
    print(grafo.raio)
    print(grafo.diametro)
    print(grafo.distancia_media)
    print("---------------------------------")