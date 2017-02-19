class Vertex:
    def __init__(self):
        self.edges = []
        self.used = False

def dfs(graph, v):
    graph[v].used = True
    for i in graph[v].edges:
        if not graph[i].used:
            dfs(graph, i)

f = open("input.txt", "r")
lines = []
for line in f:
    lines.append(line)

n, m = lines[0].split()
n = int(n)
m = int(m)
a, b = lines[-1].split()
a = int(a) - 1
b = int(b) - 1
graph = [ Vertex() for i in range(n) ]

for i in range(1, m + 1):
    u, v = lines[i].split()
    u = int(u) - 1
    v = int(v) - 1
    graph[u].edges.append(v)
    graph[v].edges.append(u)

dfs(graph, a)
if graph[b].used:
    print(1)
else:
    print(0)
