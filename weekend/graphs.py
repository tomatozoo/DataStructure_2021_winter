class graph:
    def __init__(self, g):
        self.graph = g
        self.label = []
        self.visit = [] # queue
        self.l = []
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
    def bfs(self, vertex):
        self.visit.append(vertex)
        self.l.append(vertex)
        while len(self.visit) > 0:
            tmp = self.visit.pop(0)
            print(tmp)
            for i, j in self.graph:
                if i == tmp and j not in self.l:
                    self.visit.append(j)
                    self.l.append(j)
                if j == tmp and i not in self.l:
                    self.visit.append(i)
                    self.l.append(i)
            
            
# undirected graph
gr = [(1,2), (1,4), (2,5), (2,3), (3,5), (6,9), (8,9), (10,11), (7,7)]
gr = [(1,2),(1,4), (2,5), (4,5), (3,5)]
g = graph(gr)
g.bfs(1)
