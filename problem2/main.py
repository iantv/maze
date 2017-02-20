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

f = open("input.txt", "r")
lines = [ line for line in f ]

n, m = lines[0].split()
n = int(n)
m = int(m)
a, b = lines[m + 1].split()
a = int(a) - 1
b = int(b) - 1
graph = [ Vertex() for i in range(n) ]

for i in range(1, m + 1):
    u, v = lines[i].split()
    u = int(u) - 1
    v = int(v) - 1
    graph[u].edges.append(v)
    graph[v].edges.append(u)

path = dfs(graph, a, b)
path.reverse()
if graph[b].used:
    print("path:", path)
print(int(graph[b].used))
