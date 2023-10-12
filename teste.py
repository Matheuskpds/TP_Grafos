import networkx as nx
import matplotlib.pyplot as plt  #visualizar grafo

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3)])

def contar_vertices(grafo):
    return len(grafo.nodes())

numero_de_vertices = contar_vertices(G)
print("Número de vértices:", numero_de_vertices)

print("Vizinhos do vértice 1:", list(G.neighbors(1)))

nx.draw(G, with_labels=True)
plt.show()