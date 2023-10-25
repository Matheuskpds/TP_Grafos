import networkx as nx
import matplotlib.pyplot as plt


class GrafoPonderado:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_ordem(self):
        return len(self.grafo.nodes())

    def encontrar_menor_caminho(self, origem, destino):
        try:
            shortest_path = nx.shortest_path(self.grafo, source=origem, target=destino, weight='weight')
            return shortest_path
        except nx.NetworkXNoPath:
            return "Não há caminho entre os nós."
    def printar_grafo(self):
        pos = nx.spring_layout(self.grafo)  # Layout do grafo

        # Crie um dicionário de rótulos de arestas com pesos
        edge_labels = {(u, v): d['weight'] for u, v, d in self.grafo.edges(data=True)}

        #   Desenhe o grafo
        nx.draw(self.grafo, pos, with_labels=True, node_size=700, node_color="skyblue")
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=edge_labels, font_color='red', font_size=10)
        plt.show()


G = nx.read_graphml("TP_Grafos/Código-Fonte/Grafos/grafo.graphml")
Grafo = GrafoPonderado(G)

if nx.is_weighted(G):
    print("O grafo é ponderado.")
else:
    print("O grafo não é ponderado.")
Grafo.printar_grafo()
