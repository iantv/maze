import time as time

# It's class Vertex for one Vertex in graph. Graph is array of vertex
# attributes: used, edges
# edges - nubmer of vertexes (indexes of elements in array of Vertex)
# used - bool , using in dfs for mark vertex
class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False

# It's sample dfs. Only marked vertex
# input args: graph (array of Vertex), v (int - current vertex)
def dfs(graph, v):
    graph[v].used = True
    for i in graph[v].edges:
        if not graph[i].used:
            dfs(graph, i)

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

def solve(graph):
    begin = time.clock()
    count = 0
    # If vertex not used after dfs that it's new connected component;
    # count - number of connected components
    # If vertex not used than run dfs and all vertex in current connected component are used
    for i in range(len(graph)):
        if not graph[i].used:
            dfs(graph, i)
            count += 1
    print("time: %f", begin - time.clock())
    return count
