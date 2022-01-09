class graph:
    def __init__(self, g):
        self.graph = g
        self.label = []
    def dfs(self, vertex):
        print(vertex)
        self.label.append(vertex)
        for i, j in self.graph:
            if i == vertex:
                if j not in self.label:
                    self.dfs(j)
            if j == vertex:
                if i not in self.label:
                    self.dfs(i)
    def bfs(self):
        pass
# undirected graph
gr = [(1,2), (1,4), (2,5), (2,3), (3,5), (6,9), (8,9), (10,11), (7,7)]
gr = [(1,2),(1,4), (2,5), (4,5), (3,5)]
g = graph(gr)
g.dfs(1)
g.bfs()

class Node:
    def __init__(self, value):
        self.data = value
class Graph:
    def __init__(self):
        self.graph = {}
        self.visit = []
    def create(self, v, data):
        node = Node(data)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(node)
    def dfs(self, v):
        self.visit.append(v)
        for node in self.graph[v]:
            if node.data not in self.visit:
                self.dfs(node.data)
g = Graph()
for v, node in [(1,2), (1,3), (2,1), (2,4), (2,5), (2,7), (3,1), (3,4), \
(3,5), (4,2), (4,3), (4,7), (5,2), (5,3), (5,6), (5,8), \
(6,5), (6,7), (6,8), (7,2), (7,4), (7,6), (8,5), (8,6)]:
    g.create(v, node)
g.dfs(1)
print("dfs ", g.visit)