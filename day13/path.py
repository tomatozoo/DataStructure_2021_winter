class Node:
    def __init__(self, node, weight):
        self.data = node
        self.weight = weight
class ShortestPath:
    def __init__(self):
        self.graph = {}
        self.visit = []
        self.dist = {}
        self.prev = {}
        self.min_list = {}
    
    def create(self, v, dest, weight):
        node = Node(dest, weight)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(node)
        
    def pick_min_dist(self):
        temp = []
        for v, cost in self.min_list.items():
            temp.append((cost, v))
        temp = sorted(temp)
        cost,v = temp.pop(0)
        print("Next min cost vertex is", v)
        self.min_list.pop(v)
        return v
    def dijkstra(self, v):
        if v not in self.visit:
            self.visit.append(v)
        else: return
        if v not in self.graph:
            print("end of search")
            return
        for node in self.graph[v]:
            vertex = node.data
            cost = node.weight
            if vertex not in self.dist or cost+self.dist[v]<self.dist[vertex]:
                self.dist[vertex] = cost+self.dist[v]
                self.prev[vertex] = v
                self.min_list[vertex] = cost+self.dist[v]
        self.view_array()
        v.self.pick_min_dist()
        self.dijkstra(v)

g = ShortestPath()
for start, dest, weight in [(1,2,6),(1,3,2),(1,4,16), (1,7,14), (2,4,5), (2,5,4), (3,2,7), (3,5,3), (3,6,8), (4,7,3), (5,4,4), (5,7,10), (6,7,1)]:
    g.create(start, dest, weight)
g.dist[1] = 0
g.prev[1] = None
g.dijkstra(1)