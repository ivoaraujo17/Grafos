
# cria um arquivo txt com a primeira linha contendo o número de vértices e a segunda linha contendo o número de arestas
# as próximas linhas contém as arestas do grafo

import random

def create_grafo(n):
    with open('grafo_.txt', 'w') as f:
        f.write(str(n) + '\n')
        for i in range(n):
            for j in range(n):
                if j == n-1:
                    f.write('0\n')
                else:
                    if j == i:
                        f.write('0,')
                    else:
                        f.write('1,')
        

create_grafo(100)

