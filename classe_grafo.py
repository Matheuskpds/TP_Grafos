class GrafoPonderado:
    def __init__(self, G):
        self.grafo = G
    
    def ordem_grafo(self, G):
        return len(G.nodes())
    
    def tamanho_grafo(self, G):
        return len(G.edges())

    def vizinhos_vertice(self, G, v):
        return list(G.neighbors(v))
    
    def grau_vertice(self, G, v):
        return len(G.neighbors(v))
    
    def sequencia_graus(self, G):
        return [len(G.neighbors(v)) for v in G.nodes()]