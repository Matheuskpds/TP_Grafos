import networkx as nx
import matplotlib.pyplot as plt  #visualizar grafo

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
G.add_weighted_edges_from

def contar_vertices(grafo):
    return len(grafo.nodes())

numero_de_vertices = contar_vertices(G)
print("Número de vértices:", numero_de_vertices)

nx.draw(G, with_labels=True)
plt.show()
