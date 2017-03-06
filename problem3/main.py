import time as time

class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False

def dfs(graph, v):
    graph[v].used = True
    for i in graph[v].edges:
        if not graph[i].used:
            dfs(graph, i)

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
    for i in range(len(graph)):
        if not graph[i].used:
            dfs(graph, i)
            count += 1
    print("time: %f", begin - time.clock())
    return count