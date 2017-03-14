import time as time
import sys

sys.setrecursionlimit(10000)
# Класс Vertex для описания вершины в графе. Граф - массив вершин
# Атрибуты: used(метка), edges(рёбра)
# edges - массив, состоящий из номеров вершин, к которым существует ребро
# used - bool, используется как метка, что вершина посещена/использована
class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False


# DFS. Поиск в глубину
# аргументы: graph (массив из вершин(Vertex)), v (int - текущая вершина, которую сейчас посещаем), dest (int - destination. Номер вершины к которой ищем путь)
# возвр. значения: path (путь в обратном порядке от заданной вершины v до вершины dest)
def dfs(graph, v, dest):
    graph[v].used = True
    if v == dest:
        return [v + 1]
    for i in graph[v].edges:
        if not graph[i].used:
            path = dfs(graph, i, dest)
            if len(path) > 0:
                path.append(v + 1)
                return path
    return []

# Функция инициализирующая граф данными из файла.
# аргументы: lines (массив строк из файла), m, n - число рёбер и вершин соответственно
# возвр. значения: graph (массив вершин, граф в виде списков смежности)
def graph_init(lines, n, m):
    graph = [ Vertex() for i in range(n) ]
    for i in range(1, m + 1):
        u, v = lines[i].split()
        u = int(u) - 1
        v = int(v) - 1
        graph[u].edges.append(v)
        graph[v].edges.append(u)
    return graph

# Функция для измерения времени работы программы
# аргументы: graph (граф, массив вершин), vertexA, vertexB (вершины между которыми ищем путь)
# возвр. значения: path: array of int (путь между вершинами, массив целых чисел)
def solve(graph, a, b):
    begin = time.clock()
    path = dfs(graph, a, b)
    print("time: ", abs(begin - time.clock()))
    return path
