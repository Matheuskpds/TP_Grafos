import networkx as nx
import matplotlib.pyplot as plt  #visualizar grafofrom classe_grafo import GrafoPonderado
import os

def menu():
    loop = True
    while(loop):
        print("1 - Enviar Grafo de Entrada")
        print("2 - Visualizar Grafo de Entrada")
        print("3 - Ordem do Grafo")
        print("4 - Tamanho do Grafo")
        print("5 - Vizinhos de um Vértice")
        print("6 - Grau de um Vértice")
        print("7 - Sequência de Graus")
        print("8 - Excentricidade de um vértice")
        print("9 - Raio do Grafo")
        print("10 - Diâmetro do Grafo")
        print("11 - Centro do Grafo")
        print("12 - Busca em Lagura")
        print("13 - Distância e Caminho Mínimo")
        print("14 - Centralidade de Proximidade C de um vértice")
        print("15 - Encerrar Programa")
        resposta = int(input("Digite a opção desejada: "))
        os.system('cls')

        if resposta == 1:
            Grafo = nx.read_graphml("..\TP_Grafos\grafo.graphml")

        if resposta == 2:
            pos = nx.spring_layout(Grafo)  # Layout do grafo
            if nx.is_weighted(Grafo):
                edge_labels = {(u, v): Grafo.edges[u, v]['weight'] for u, v, d in Grafo.edges(data=True)}
            else:
                edge_labels = {}
            nx.draw(Grafo, pos, with_labels=True, node_size=700, node_color="skyblue")
            nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels, font_color='red', font_size=10)
            plt.show()
        if resposta == 3:
            print("A ordem do grafo é: ", nx.number_of_nodes(Grafo))
        if resposta == 4:
            print("O tamanho do grafo é: ", (nx.number_of_edges(Grafo) + nx.number_of_nodes(Grafo)))
        if resposta == 5: 
            vertice = str(input("Digite um vértice para saber seus vizinhos: "))
            print("O(s) vizinho(s) do vértice " + vertice + " são: ", list(nx.neighbors(Grafo, vertice)))
        if resposta == 6:
            vertice = str(input("Digite um vértice para saber o seu grau: "))
            print("O grau do vértice " + vertice + " é: ", nx.degree(Grafo, vertice))
        if resposta == 7:
            seq_graus = [val for (node, val) in nx.degree(Grafo)]
            print("A sequência de graus do grafo é: ", sorted(seq_graus, reverse=True))
        if resposta == 8:
            vertice = str(input("Digite um vértice para saber o sua excentricidade: "))
            print("A excentricidade do vértice " + vertice + " é: ", nx.eccentricity(Grafo, vertice))
        if resposta == 9:
            print("O raio do grafo é: ", nx.radius(Grafo))
        if resposta == 10:
            print("O diâmetro do grafo é: ", nx.diameter(Grafo))
        if resposta == 11:
            print("O centro do grafo é: ", nx.center(Grafo))
        if resposta == 12:
            vertice = str(input("Digite um vértice para iniciar a busca em largura: "))
            BuscaLargura = nx.bfs_tree(Grafo, vertice)
            arestas_fora_arvore = [(u, v) for u, v in Grafo.edges() if (u, v) not in BuscaLargura.edges()]
            print("Sequencia de vértices visitados na busca em largura: ", list(BuscaLargura))
            print("Arestas que não fazem parte da árvore de busca em largura: ", arestas_fora_arvore)
            nx.write_graphml(BuscaLargura, "TP_Grafos/Arvore_Busca_em_Largura.graphml")
        if resposta == 13:
            resultados_dijkstra = dict(nx.all_pairs_dijkstra_path(Grafo))
            for origem, destinos in resultados_dijkstra.items():
                print(f"Distância de {origem} a:")
                for destino, caminho in destinos.items():
                    if origem != destino:
                        distancia = sum(Grafo[u][v].get('weight', 1) for u, v in zip(caminho[:-1], caminho[1:]))
                        print(f"{destino}: {caminho} com distância {distancia}")
        if resposta == 14:
            vertice = str(input("Digite um vértice para saber sua centralidade de proximidade: "))
            distancias_minimas = nx.single_source_dijkstra_path_length(Grafo, vertice)
            distanciaTotal = sum(distancias_minimas.values())
            centralidade = (nx.number_of_nodes(Grafo) - 1) / distanciaTotal
            print("A centralidade de proximidade do vértice " + vertice + f" é: {centralidade:.4f}")
        if resposta == 15:
            print("Encerrando programa...")
            loop = False

menu()