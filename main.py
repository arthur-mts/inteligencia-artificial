from models.graph import Grafo
from utils.csv_reader import CsvReader

reader = CsvReader("files/heuristica_final.csv", "files/arestas_final.csv")


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
        if n == b:
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

    para_percorrer = set()
    veio_de = {}
    g_score = {}
    f_score = {}

    vertice_cor = a

    para_percorrer.add(vertice_cor)

    g_score[vertice_cor] = 0
    f_score[vertice_cor] = h(vertice_cor)

    while para_percorrer:

        vertice_cor = min(para_percorrer, key=lambda o: f_score[o])
        if vertice_cor == b:
            return reconstroi_caminho(veio_de, vertice_cor)

        para_percorrer.remove(vertice_cor)

        for vizinho in grafo.arestas_sobre_vertice(vertice_cor):
            tentativa = -1 if g_score.get(vertice_cor) is None else g_score.get(vertice_cor) + grafo.valor_aresta(
                f"{vertice_cor}-{vizinho}")

            g_score_c = -1 if g_score.get(vizinho) is None else g_score.get(vizinho)
            if g_score_c == -1 or tentativa < g_score_c:
                veio_de[vizinho] = vertice_cor
                g_score[vizinho] = tentativa
                f_score[vizinho] = g_score_c + h(vizinho)

                para_percorrer.add(vizinho)
    raise Exception()


def h(vertice):
    return reader.ler_tabela_heuristica()[vertice]


def main():
    ## Montando objeto do grafo
    grafo = Grafo(reader.ler_vertices())
    for aresta_c in reader.ler_arestas():
        grafo.adicionaAresta(aresta_c["aresta"], aresta_c["distancia"])
    origem = "Caruaru"
    destino = "Recife"
    print(f"Calculando caminho entre {origem} e {destino}")

    print("Algoritmo de Deep Search: ", deep_search(grafo, origem, destino))
    print("Algoritmo de BFS:", bfs(grafo, origem, destino))
    print("Algoritmo A*: ", a_star(origem, destino, grafo, h))


if __name__ == '__main__':
    main()
