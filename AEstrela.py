import numpy as np


class Vertice:

    def __init__(self, cidade, distancia):
        self.cidade = cidade
        self.visitado = False
        self.distancia = distancia
        self.adjacentes = []

    def adiciona_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice.cidade, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia + self.custo


class Grafo:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.adiciona_adjacentes(Adjacente(zerind, 75))
    arad.adiciona_adjacentes(Adjacente(sibiu, 140))
    arad.adiciona_adjacentes(Adjacente(timisoara, 118))

    zerind.adiciona_adjacentes(Adjacente(arad, 75))
    zerind.adiciona_adjacentes(Adjacente(oradea, 71))

    oradea.adiciona_adjacentes(Adjacente(zerind, 71))
    oradea.adiciona_adjacentes(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacentes(Adjacente(oradea, 151))
    sibiu.adiciona_adjacentes(Adjacente(arad, 140))
    sibiu.adiciona_adjacentes(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacentes(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacentes(Adjacente(arad, 118))
    timisoara.adiciona_adjacentes(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacentes(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacentes(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacentes(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacentes(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacentes(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacentes(Adjacente(craiova, 120))

    craiova.adiciona_adjacentes(Adjacente(dobreta, 120))
    craiova.adiciona_adjacentes(Adjacente(pitesti, 138))
    craiova.adiciona_adjacentes(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacentes(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacentes(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacentes(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacentes(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacentes(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacentes(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacentes(Adjacente(craiova, 138))
    pitesti.adiciona_adjacentes(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacentes(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacentes(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacentes(Adjacente(giurgiu, 90))


grafo = Grafo()


class VetorOrdenado:
    # Armazena as cidades adjacentes
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):  # Percorre o vetor
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:  # Caso para atualizar a ultima posição
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]  # Desloca os valores para inserção
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.cidade, ' : ',
                      self.valores[i].custo, '(Em Linha reta) + ',
                      self.valores[i].vertice.distancia, '(Distancia do objetivo) = distancia AEstrela: ',
                      self.valores[i].distancia_aestrela)


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):  # Função de teste de objetivo
        print('------')
        print('Atual: {}'.format(atual.cidade))
        atual.visitado = True  # Marca o atual como visitado

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))  # Cria um vetor com o tamanho da quantidade
            for adjacente in atual.adjacentes:  # Percorre a lista de vizinhos do grafo atual
                if adjacente.vertice.visitado == False:  # se o vizinho ainda não foi visitado
                    adjacente.vertice.visitado = True  # Marcar como visitado
                    vetor_ordenado.insere(adjacente)  # insere dentro do vetor ordenado como vizinho do nó atual
            vetor_ordenado.imprime()  # Mostra os vizinhos do nó atual

            if vetor_ordenado.valores[0] != None:  # Se o conteúdo não for nulo
                self.buscar(vetor_ordenado.valores[0].vertice)  # Busca pelo inicio do vetor ordenado


def main():
    busca_aestrela = AEstrela(grafo.bucharest)
    busca_aestrela.buscar(grafo.arad)


if __name__ == '__main__':
    main()
