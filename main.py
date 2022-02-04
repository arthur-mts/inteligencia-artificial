from queue import Queue

from models.graph import Grafo


# def a_star(a, b):
#
#
#
#
def deep_search(a, b):

def bfs(grafo: Grafo, a, b):
    if not (grafo.existeVertice(a) and grafo.existeVertice(b)):
        raise Exception("Verices invalidos")
    n = a
    visitados = [n]
    caminho = [n]
    while caminho:
        n = caminho.pop(0)
        vertices_adj = list(map(lambda i: i["value"], grafo.arestas_sobre_vertice_bfs(n)))
        for i in vertices_adj:
            if n == b:
                return visitados
            if i not in visitados:
                caminho.append(i)
                visitados.append(i)


def main():
    grafo = Grafo(["A", "B", "C"])
    grafo.adicionaAresta("A-B", 5)
    grafo.adicionaAresta("A-C", 2)
    print(bfs(grafo, 'A', 'C'))


if __name__ == '__main__':
    main()
