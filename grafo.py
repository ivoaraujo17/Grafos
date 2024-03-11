from busca_largura import busca_em_largura
class graph:
    def __init__(self, graph_txt):
        self.num_vertices = None
        self.matriz_adjacencia = None
        self.lista_adjacencia = None
        self.read_graph(graph_txt)
        self.nome_arquivo = str(graph_txt).split(".")[0]
        self.distancia_media = None
        self.raio = None
        self.diametro = None
        self.metricas()
    
    def read_graph(self, graph):
        # leitura do arquivo txt
        with open(graph, 'r') as arquivo:
            matriz_adjacencia = []
            lista_adjacencia = []

            arquivo = arquivo.readlines()
            num_vertices = int(arquivo[0]) 
            for linha in arquivo[1:]:
                linha = linha.strip().split(' ')
                linha = [int(i) for i in linha]

                matriz_adjacencia.append(linha)

                lista_aux = []
                for i in range(len(linha)):
                    if linha[i] != 0:
                        lista_aux.append(i)
                lista_adjacencia.append(lista_aux)

            self.num_vertices = num_vertices
            self.matriz_adjacencia = matriz_adjacencia
            self.lista_adjacencia = lista_adjacencia
    
    def print_matrix(self):
        print('\nMatriz de Adjacencia')
        for linha in self.matriz_adjacencia:
            print(linha)
        print()
    
    def print_lista_adjacencia(self):
        print('\nLista de Adjacencia')
        for lista in self.lista_adjacencia:
            print(lista)
        print()

        
    def metricas(self):
        distancia = 0
        self.raio = self.num_vertices
        self.diametro = 0
        pares = 0
        for i in range(self.num_vertices):
            busca = busca_em_largura(self)
            busca.inicializa(i+1)
            if busca.excentricidade < self.raio:
                self.raio = busca.excentricidade
            if busca.excentricidade > self.diametro:
                self.diametro = busca.excentricidade    
            for j in range(i+1, self.num_vertices):
                distancia += busca.nivel_vertice[j]
                pares += 1
        self.distancia_media = distancia / pares
    