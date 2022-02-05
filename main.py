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
        if d == b:
            return 0
        aresta = f"{n}-{d}"
        if not grafo.existeAresta(aresta):
            raise Exception
        return h(n) + grafo.valor_aresta(aresta)

    def reconstroi_caminho(_veio_de, corrente):
        caminho_final = []
        while corrente in _veio_de.keys():
            corrente = _veio_de[corrente]
            caminho_final = [corrente] + caminho_final
            caminho_final.append(b)
        return caminho_final

    percordidos = set()
    veio_de = {}
    g_score = {}

    vertice_cor = a

    percordidos.add(vertice_cor)

    g_score[vertice_cor] = 0

    while percordidos:
        vertice_cor = min(percordidos, key=lambda o: f(o, b))
        if vertice_cor == b:
            return reconstroi_caminho(veio_de, vertice_cor)

        percordidos.remove(vertice_cor)

        for vizinho in grafo.arestas_sobre_vertice(vertice_cor):
            tentativa = -1 if g_score.get(vertice_cor) is None else g_score.get(vertice_cor) + grafo.valor_aresta(
                f"{vertice_cor}-{vizinho}")

            g_score_c = -1 if g_score.get(vizinho) is None else g_score.get(vizinho)
            if g_score_c == -1 or tentativa < g_score_c:
                veio_de[vizinho] = vertice_cor
                g_score[vizinho] = tentativa

                percordidos.add(vizinho)
    raise Exception()


def h(vertice):
    return {
        "RMG": 0,
        "AREIA": 2,
        "ESP": 1,
        "LDM": 2
    }[vertice]


def main():
    grafo = Grafo(["RMG", "ESP", "AREIA", "LDM"])
    grafo.adicionaAresta("RMG-ESP", 5)
    grafo.adicionaAresta("RMG-AREIA", 2)
    grafo.adicionaAresta("LDM-RMG", 2)
    grafo.adicionaAresta("AREIA-LDM", 1)
    print(a_star("AREIA", "RMG", grafo, h))


if __name__ == '__main__':
    main()
