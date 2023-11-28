from classe_grafo import GrafoPonderado
import networkx as nx
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
        print("15 - Verificar se o grafo eh um ciclo")
        print("16 - Encontrar o menor ciclo do grafo")
        print("17 - Árvore Geradora Mínima")
        print("18 - Determinar um conjunto estável de vértices de um grafo por meio de uma heurística")
        print("19 - Determinar Emparelhamento Máximo do Grafo")
        print("20 - Encontrar Ciclo Mínimo do Grafo")
        print("21 - Checar se há ciclos no grafo")
        print("22 - Encerrar Programa")
        resposta = int(input("Digite a opção desejada: "))
        os.system('cls')

        if resposta == 1:
            print("Obs: O grafo precisa estar adicionado na no caminho TP_Grafos/Código-Fonte/Grafos/")
            Arquivo_Grafo = str(input("Digite o nome do arquivo do grafo: "))
            G = nx.read_graphml("../TP_Grafos/Código-Fonte/Grafos/" + Arquivo_Grafo)
            Grafo = GrafoPonderado(G)
        if resposta == 2:
            Grafo.printar_grafo(G)
        if resposta == 3:
            print("A ordem do grafo é: ", Grafo.ordem_grafo())
        if resposta == 4:
            print("O tamanho do grafo é: ", Grafo.tamanho_grafo())
        if resposta == 5: 
            vertice = str(input("Digite um vértice para saber seus vizinhos: "))
            print("O(s) vizinho(s) do vértice " + vertice + " são: ", Grafo.vizinhos_vertice(vertice))
        if resposta == 6:
            vertice = str(input("Digite um vértice para saber o seu grau: "))
            print("O grau do vértice " + vertice + " é: ", Grafo.grau_vertice(vertice))
        if resposta == 7:
            print("A sequência de graus do grafo é: ", Grafo.sequencia_graus())
        if resposta == 8:
            vertice = str(input("Digite um vértice para saber o sua excentricidade: "))
            print("A excentricidade do vértice " + vertice + " é: ", Grafo.excen_vertice(vertice))
        if resposta == 9:
            print("O raio do grafo é: ", Grafo.raio_grafo())
        if resposta == 10:
            print("O diâmetro do grafo é: ", Grafo.diametro_grafo())
        if resposta == 11:
            print("O centro do grafo é: ", Grafo.centro_grafo())
        if resposta == 12:
            vertice = str(input("Digite um vértice para iniciar a busca em largura: "))
            Grafo.busca_largura(vertice)
        if resposta == 13:
            Grafo.distancia_caminho_minimo()
        if resposta == 14:
            vertice = str(input("Digite um vértice para saber sua centralidade de proximidade: "))
            Grafo.centralidade_proximidade(vertice)
        if resposta == 17:
            Grafo.arvore_geradora_minima()
        if resposta == 18:
            conjunto_independente, numero_independencia = Grafo.conjunto_estavel()
            print("Conjunto Independente:", conjunto_independente)
            print("Número de Independência:", numero_independencia)
        if resposta == 19:
            print("O emparelhamento máximo é formado pelas arestas:", Grafo.emparelhamento_maximo())
        if resposta == 20:
            print("O menor cíclo deste grafo é formado pelas arestas:", Grafo.encontrar_menor_ciclo())
        if resposta == 21:
            Grafo.encontrar_ciclo()
        if resposta == 22:
            print("Encerrando programa...")
            loop = False
        if(resposta > 22 or resposta < 1):
            print("Opção inválida, tente novamente!")
        if(resposta != 20):
            aux = str(input("Aperte qualquer tecla para continuar... "))
            os.system('cls')


       

menu()