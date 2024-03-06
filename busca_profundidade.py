from grafo import graph
from collections import deque

class busca_em_profundidade:
    VERMELHO = '255,0,0'
    AZUL = '0,0,255'

    def __init__(self, graph:graph) -> None:
        self.graph = graph
        self.cores = None
        self.pai_list = None
        self.profundidade_entrada = None
        self.profundidade_saida = None
        self.__init_atributos()
        self.tempo = 0
        
    def __init_atributos(self):
        matriz = []
        pais = []
        profundidade_entrada = []
        profundidade_saida = []
        for linha in range(self.graph.num_vertices):
            l = []
            for vertice in range(self.graph.num_vertices):
                l.append(None)
            matriz.append(l)
            pais.append(None)
            profundidade_entrada.append(0)
            profundidade_saida.append(0)
        self.cores = matriz
        self.pai_list = pais
        self.profundidade_entrada = profundidade_entrada
        self.profundidade_saida = profundidade_saida
    
    def inicializa(self, vertice_inicial):
        if not (vertice_inicial <= self.graph.num_vertices \
            and vertice_inicial >= 1):
            raise 'numero de vertice invalido'
        vertice_atual = vertice_inicial - 1
        while 0 in self.profundidade_entrada:
            # cria uma nova raiz para cada arvore independente do grafo
            self.tempo += 1
            self.profundidade_entrada[vertice_atual] = self.tempo
            self.__busca(vertice_atual)
        
    def __busca(self, vertice):
        vertice_atual = vertice
        for vizinho in self.graph.lista_adjacencia[vertice_atual]:
            if self.profundidade_entrada[vizinho] == 0:
                # vizinho recebe como pai o vertice atual
                self.pai_list[vizinho] = vertice_atual
                # pintando a aresta do pai para o filho
                self.cores[vertice_atual][vizinho] = self.AZUL
                # incrementando o tempo
                self.tempo += 1
                self.profundidade_entrada[vizinho] = self.tempo
                self.__busca(vizinho)
            else:
                # Teste para saber se é uma aresta de retorno
                if self.profundidade_saida[vizinho] == 0 and vizinho != self.pai_list[vertice_atual]:
                    self.cores[vertice_atual][vizinho] = self.VERMELHO
        
        self.tempo += 1
        self.profundidade_saida[vertice_atual] = self.tempo
        print(self.pai_list)
        #print(self.cores)


grafo = graph('grafo.txt')
busca = busca_em_profundidade(grafo)
busca.inicializa(1)





