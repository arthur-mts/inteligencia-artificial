import csv


class CsvReader:
    def __init__(self, heuristica_path, arestas_path):
        self.heuristica_path = heuristica_path
        self.arestas_path = arestas_path

    def ler_arestas(self):
        arestas = []
        with open(self.arestas_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    arestas.append({
                        "aresta": row[0],
                        "distancia": int(row[1])
                    })
        return arestas

    def ler_tabela_heuristica(self):
        heuristica = {}
        with open(self.heuristica_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    heuristica[row[0]] = int(row[1])
        return heuristica

    def ler_vertices(self):
        vertices = []
        with open(self.heuristica_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    vertices.append(row[0])

        return vertices
