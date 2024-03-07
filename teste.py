from grafo import graph
from busca_largura import busca_em_largura

grafo = graph("in/graph_19")
#busca = busca_em_largura(grafo)
#busca.inicializa(1)
print(grafo.raio)
print(grafo.diametro)
print(grafo.distancia_media)