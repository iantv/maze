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
# возвр. значения: отсутстуют, т.к. необходимо только пометить вершину, что она посещена
def dfs(graph, v):
    graph[v].used = True
    for i in graph[v].edges:
        if not graph[i].used:
            dfs(graph, i)


# Функция инициализирующая граф данными из файла.
# аргументы: lines (массив строк из файла), m, n - число рёбер и вершин соответственно
# возвр. значения: graph (массив вершин, граф хранится в виде списков смежности)
def graph_init(lines, n, m):
    graph = [ Vertex() for i in range(n) ]
    for i in range(1, m + 1):
        u, v = lines[i].split()
        u = int(u) - 1
        v = int(v) - 1
        graph[u].edges.append(v)
        graph[v].edges.append(u)
    return graph

def solve(graph):
    begin = time.clock()
    count = 0
    # Если вершина не является помеченной, то она не принадлежит ни одной компонентой связности
    # т.к. dfs гарантирует обход всего графа, следовательно все вершины одной компоненты будут помещены
    # count - число компонент связности. Каждый dfs вызывается на новой компоненте, раннее не посещённой
    # graph[i].used - true если вершина посещена раннее, false иначе.
    for i in range(len(graph)):
        if not graph[i].used:
            dfs(graph, i)
            count += 1
    print("time: ", abs(time.clock() - begin))
    return count
