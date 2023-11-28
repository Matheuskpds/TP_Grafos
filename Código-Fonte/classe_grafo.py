import networkx as nx
import matplotlib.pyplot as plt  #visualizar grafofrom classe_grafo import GrafoPonderado
import os

class GrafoPonderado:
    def __init__(self, G):
        self.grafo = G

    def printar_grafo(self, G):
        pos = nx.spring_layout(G)  # Layout do grafo

        # Crie um dicionário de rótulos de arestas com pesos
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

        #   Desenhe o grafo
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
        plt.show()
    
    def ordem_grafo(self):
        return nx.number_of_nodes(self.grafo)
    
    def tamanho_grafo(self):
        return nx.number_of_edges(self.grafo) + nx.number_of_nodes(self.grafo)

    def vizinhos_vertice(self, v):
        return list(nx.neighbors(self.grafo, v))
    
    def grau_vertice(self, v):
        return nx.degree(self.grafo, v)
    
    def sequencia_graus(self):
        seq_graus = [val for (node, val) in nx.degree(self.grafo)]
        return sorted(seq_graus, reverse=True)
    
    def excen_vertice(self, v):
        return nx.eccentricity(self.grafo, v)
    
    def raio_grafo(self):
        return nx.radius(self.grafo)
    
    def diametro_grafo(self):
        return nx.diameter(self.grafo)
    
    def centro_grafo(self):
        return nx.center(self.grafo)
    
    def busca_largura(self, v):
        BuscaLargura = nx.bfs_tree(self.grafo, v)
        arestas_fora_arvore = [(u, v) for u, v in self.grafo.edges() if (u, v) not in BuscaLargura.edges()]
        print("Sequencia de vértices visitados na busca em largura: ", list(BuscaLargura))
        print("Arestas que não fazem parte da árvore de busca em largura: ", arestas_fora_arvore)
        nx.write_graphml(BuscaLargura, "TP_Grafos/Código-Fonte/Grafos/Arvore_Busca_em_Largura.graphml")
        resposta = str(input("Deseja visualizar a árvore de busca em largura? (S/N)"))
        if resposta == 'S' or resposta == 's':
            Arvore_Busca_Largura = nx.read_graphml("TP_Grafos/Código-Fonte/Grafos/Arvore_Busca_em_Largura.graphml")
            if nx.is_weighted(Arvore_Busca_Largura):
                self.printar_grafo(Arvore_Busca_Largura)
            else:
                nx.draw(Arvore_Busca_Largura, with_labels=True)
                plt.show()
            
    def distancia_caminho_minimo(self):
        #algoritmo de dijkstra
        resultados_dijkstra = dict(nx.all_pairs_dijkstra_path(self.grafo))
        for origem, destinos in resultados_dijkstra.items():
            print(f"Distância de {origem} a:")
            for destino, caminho in destinos.items():
                if origem != destino:
                    distancia = sum(self.grafo[u][v].get('weight', 1) for u, v in zip(caminho[:-1], caminho[1:]))
                    print(f"{destino}: {caminho} com distância {distancia}")
    
    def centralidade_proximidade(self, v):
        distancias_minimas = nx.single_source_dijkstra_path_length(self.grafo, v)
        distanciaTotal = sum(distancias_minimas.values())
        centralidade = (nx.number_of_nodes(self.grafo) - 1) / distanciaTotal
        print("A centralidade de proximidade do vértice " + v + f" é: {centralidade:.4f}")

    #def eh_ciclo(self):

    #def menor_ciclo(self):

    def arvore_geradora_minima(self):
        Arvore_Geradora_Minima = nx.minimum_spanning_tree(self.grafo)
        nx.write_graphml(Arvore_Geradora_Minima, "TP_Grafos/Código-Fonte/Grafos/Arvore_Geradora_Minima.graphml")
        resposta = str(input("Deseja visualizar a árvore geradora mínima? (S/N)"))
        if (resposta == 'S' or resposta == 's'):
            Arvore_Geradora_Minima_Graphml = nx.read_graphml("TP_Grafos/Código-Fonte/Grafos/Arvore_Geradora_Minima.graphml")
            if nx.is_weighted(Arvore_Geradora_Minima_Graphml):
                self.printar_grafo(Arvore_Geradora_Minima_Graphml)
            else:
                nx.draw(Arvore_Geradora_Minima_Graphml, with_labels=True)
                plt.show()

    def conjunto_estavel(self):
        # Inicializa os conjuntos
        N = set(self.grafo.nodes())
        S = set()
        a = 0

        while len(N) > 0:
            xk = max(N, key=lambda x: self.grafo.degree(x))
            neighbors = set([xk] + list(self.grafo.neighbors(xk)))
            N -= neighbors
            S.add(xk)
            a += 1

        return S, a


    def emparelhamento_maximo(self):
        return nx.algorithms.matching.max_weight_matching(self.grafo)
        
    def encontrar_menor_ciclo(self):
        return minimum_cycle_basis(self.grafo)