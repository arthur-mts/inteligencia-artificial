from models.graph import Grafo


def deep_search(grafo, a, b):
    caminho = []

    def deep_search_util(_visitados, _n):
        _visitados.add(_n)
        caminho.append(_n)
        if _n == b:
            return caminho
        vertices_adj = grafo.arestas_sobre_vertice(_n)
        for _i in vertices_adj:
            if _i not in visitados:
                return deep_search_util(visitados, _i)

    if not (grafo.existeVertice(a) and grafo.existeVertice(b)):
        raise Exception("Verices invalidos")

    visitados = set()
    return deep_search_util(visitados, a)


def bfs(grafo: Grafo, a, b):
    if not (grafo.existeVertice(a) and grafo.existeVertice(b)):
        raise Exception("Verices invalidos")
    n = a
    visitados = [n]
    caminho = [n]
    while caminho:
        n = caminho.pop(0)
        vertices_adj = grafo.arestas_sobre_vertice(n)
        for i in vertices_adj:
            if i not in visitados:
                caminho.append(i)
                visitados.append(i)

                if i == b:
                    return visitados


def a_star(a, b, grafo: Grafo, h):
    def f(n, d):
        aresta = f"{n}-{d}"
        if not grafo.existeAresta(aresta):
            raise Exception
        return h(n) + grafo.valorAresta(aresta)

    def reconstroiCaminho(_veio_de, corrente):
        caminho_final = []
        while corrente in _veio_de.keys():
            corrente = _veio_de[corrente]
            caminho_final = [corrente] + caminho_final
        return caminho_final

    percordidos = set()
    n_percoridos = set()
    veio_de = {}

    vertice_cor = a

    percordidos.add(vertice_cor)
    while percordidos:
        vertice_cor = min(percordidos, key = lambda o : f(o, b))
        if vertice_cor == b:
            return reconstroiCaminho(veio_de, vertice_cor)

        percordidos.remove(vertice_cor)

        for vizinho in grafo.arestas_sobre_vertice(vertice_cor):






    while vertice_cor !=
    adjacentes = grafo.arestas_sobre_vertice(a)


    menor_dis = None
    menor_adj = None
    for adj in adjacentes:
        cur_dis = f(a, adj)
        if menor_dis is None or cur_dis < menor_dis:
            menor_adj = adj
            menor_dis = cur_dis


def main():
    grafo = Grafo(["RMG", "ESP", "AREIA"])
    grafo.adicionaAresta("RMG-ESP", 5)
    grafo.adicionaAresta("RMG-AREIA", 2)
    print(bfs(grafo, 'RMG', 'ESP'))
    print(deep_search(grafo, 'RMG', 'ESP'))


if __name__ == '__main__':
    main()
