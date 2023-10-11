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
        pos = nx.spring_layout(G)  # Layout do grafo

        # Crie um dicionário de rótulos de arestas com pesos
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

        #   Desenhe o grafo
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
        plt.show()

    # Adicione mais métodos conforme necessário

G = nx.Graph()
G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=3)
G.add_edge(1, 3, weight=7)

Grafo = GrafoPonderado(G)

ordem = Grafo.calcular_ordem()
print("Ordem do grafo:", ordem)

menor_caminho = Grafo.encontrar_menor_caminho(1, 3)
print("Menor caminho:", menor_caminho)

Grafo.printar_grafo()