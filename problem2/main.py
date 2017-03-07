import time as time

# It's class Vertex for one Vertex in graph. Graph is array of vertex
# attributes: used, edges
# edges - nubmer of vertexes (indexes elements in array of Vertex)
# used - bool , using in dfs for mark vertex
class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False


# It's DFS
# input args: graph (array of Vertex), v (int - current vertex), dest (int - destination)
# output args: path (array of int - reverse path from v to dest)
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

# It's function for initialization graph. Graph represented as lists
# input args: lines (array of string from test file)
# output args: graph (array of Vertex)
def graph_init(lines, n, m):
    graph = [ Vertex() for i in range(n) ]
    for i in range(1, m + 1):
        u, v = lines[i].split()
        u = int(u) - 1
        v = int(v) - 1
        graph[u].edges.append(v)
        graph[v].edges.append(u)
    return graph

# It's function for check execution time and run dfs
# input args: graph (array of Vertex), vertexA, vertexB (int)
# output args: path: array of int (number of vertexes)
def solve(graph, a, b):
    begin = time.clock()
    path = dfs(graph, a, b)
    print("time: ", begin - time.clock())
    return path
