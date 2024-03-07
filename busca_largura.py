import queue

class busca_em_largura:
    VERMELHO = '255,0,0'
    AZUL = '0,0,255'
    VERDE = '0,255,0'
    AMARELO = '255,255,0'

    def __init__(self, graph) -> None:
        self.graph = graph
        self.cores = None
        self.pai_list = None
        self.relogio_vertice = None
        self.nivel_vertice = None
        self.__init_atributos()
        self.tempo = 0
        self.excentricidade = None
        
    def __init_atributos(self):
        matriz = []
        pais = []
        relogio_vertice = []
        nivel_vertice = []
        for linha in range(self.graph.num_vertices):
            l = []
            for vertice in range(self.graph.num_vertices):
                l.append(None)
            matriz.append(l)
            pais.append(None)
            relogio_vertice.append(0)
            nivel_vertice.append(0)
        self.cores = matriz
        self.pai_list = pais
        self.relogio_vertice = relogio_vertice
        self.nivel_vertice = nivel_vertice

    def inicializa(self, vertice_inicial):
        if not (vertice_inicial <= self.graph.num_vertices \
            and vertice_inicial >= 1):
            raise 'numero de vertice invalido'
        vertice_atual = vertice_inicial - 1
        while 0 in self.relogio_vertice:
            # cria uma nova raiz para cada arvore independente do grafo
            self.nivel_vertice[vertice_atual] = 0
            self.tempo += 1
            self.relogio_vertice[vertice_atual] = self.tempo
            self.__busca(vertice_atual)
            try:
                vertice_atual = self.relogio_vertice.index(0)
            except:
                continue
        self.__constroi_resultado()
        self.excentricidade = max(self.nivel_vertice)   
        

    def __busca(self, vertice):
        fila = queue.Queue()
        fila.put(vertice)
        while not fila.empty():
            vertice_atual = fila.get()
            for vizinho in self.graph.lista_adjacencia[vertice_atual]:
                if self.relogio_vertice[vizinho] == 0:
                    # vizinho recebe como pai o vertice atual
                    self.pai_list[vizinho] = vertice_atual
                    self.cores[vertice_atual][vizinho] = self.AZUL
                    self.cores[vizinho][vertice_atual] = self.AZUL
                    # o nivel do vizinho recebe o nivel do pai + 1
                    self.nivel_vertice[vizinho] = self.nivel_vertice[vertice_atual] + 1
                    # incrementa o tempo
                    self.tempo += 1
                    # o tempo do vizinho recebe tempo
                    self.relogio_vertice[vizinho] = self.tempo
                    # coloca o vizinho na fila
                    fila.put(vizinho)
                else:
                    # se o vizinho está no mesmo vertice, verifica se é irmao ou primo
                    if self.nivel_vertice[vizinho] == self.nivel_vertice[vertice_atual]:
                        # se o vizinho tem o mesmo pai do vertice atual, então é irmão
                        if self.pai_list[vizinho] == self.pai_list[vertice_atual]:
                            self.cores[vertice_atual][vizinho] = self.VERMELHO
                            self.cores[vizinho][vertice_atual] = self.VERMELHO
                        else:
                            # se tem pais diferentes, são primos
                            self.cores[vertice_atual][vizinho] = self.AMARELO
                            self.cores[vizinho][vertice_atual] = self.AMARELO
                    
                    # se o vizinho está em um nivel abaixo do vertice atual, então o atual é tio
                    elif self.nivel_vertice[vizinho] == self.nivel_vertice[vertice_atual] + 1:
                        self.cores[vertice_atual][vizinho] = self.VERDE
                        self.cores[vizinho][vertice_atual] = self.VERDE

    def __constroi_resultado(self):
        nome_arquivo_resultado = self.graph.nome_arquivo + "_bfs.gdf"

        with open(nome_arquivo_resultado, "w") as arquivo:
            arquivo.write("nodedef>name VARCHAR,label VARCHAR\n")

            for i in range(len(self.graph.matriz_adjacencia)):
                arquivo.write(f"{i+1},{i+1}\n")
            
            arquivo.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n")

            for i in range(len(self.cores)):
                for j in range(i, len(self.cores)):
                    if self.cores[i][j] != None:
                        arquivo.write(f"{i+1},{j+1},false,'{self.cores[i][j]}'\n")

