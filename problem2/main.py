import time as time

class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False

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

def graph_init(lines, n, m):
    graph = [ Vertex() for i in range(n) ]
    for i in range(1, m + 1):
        u, v = lines[i].split()
        u = int(u) - 1
        v = int(v) - 1
        graph[u].edges.append(v)
        graph[v].edges.append(u)
    return graph

def solve(graph, a, b):
    begin = time.clock()
    path = dfs(graph, a, b)
    print("time: %f", begin - time.clock())
    return path
    
