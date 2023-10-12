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
            Grafo = nx.read_graphml("TP_Grafos/teste.graphml")

        if resposta == 2:
            pos = nx.spring_layout(Grafo)  # Layout do grafo
            if nx.is_weighted(Grafo):
                edge_labels = {(u, v): d.get('weight', '') for u, v, d in Grafo.edges(data=True)}
            else:
                edge_labels = {}
            nx.draw(Grafo, pos, with_labels=True, node_size=700, node_color="skyblue")
            nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels, font_color='red', font_size=10)
            plt.show()

            

        if resposta == 15:
            print("Encerrando programa...")
            loop = False

menu()