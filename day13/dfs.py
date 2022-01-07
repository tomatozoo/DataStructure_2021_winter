class Node:
    def __init__(self, value):
        self.data = value
class Graph:
    def __init__(self):
        self.graph= {}
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
for v, node in [(1,2),(1,3), (2,1), (2,4), (2,5), (2,7), (3,1), (3,4), \
    (3,5), (4,2), (4,3), (4,7), (5,2), (5,3), (5,6), (5,8), (6,5), (6,7), (6,8), (7,2), (7,4), (7,6), (8,5), (8,6)]:
    g.create(v, node)

g.dfs(1)
print("dfs ", g.visit)

class Graph:
    def __init__(self):
        self.graph= {}
        self.visit = []
        self.queue = []
    def create(self, v, data):
        node = Node(data)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(node)
    def addq(self, v):
        self.queue.append(v)
    def deleteq(self):
        if self.queue: return self.queue.pop(0)
        else:
            print("Queue Empty")
    
    def bfs(self, v):
        self.visit.append(v)
        self.addq(v)
        while self.queue:
            v = self.deleteq()
            for node in self.graph[v]:
                if node.data not in self.visit:
                    self.visit.append(node.data)
                    self.addq(node.data)

g = Graph()
for v, node in [(1,2),(1,3), (2,1), (2,4), (2,5), (2,7), (3,1), (3,4), \
    (3,5), (4,2), (4,3), (4,7), (5,2), (5,3), (5,6), (5,8), (6,5), (6,7), (6,8), (7,2), (7,4), (7,6), (8,5), (8,6)]:
    g.create(v, node)
g.visit=[]
g.bfs(1)
print("bfs ", g.visit)