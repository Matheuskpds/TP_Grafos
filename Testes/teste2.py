import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=3)
G.add_edge(1, 3, weight=7)

pos = nx.spring_layout(G)  # Layout do grafo

# Crie um dicionário de rótulos de arestas com pesos
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.write_graphml(G, "grafo.graphml")
# Desenhe o grafo
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

plt.show()
