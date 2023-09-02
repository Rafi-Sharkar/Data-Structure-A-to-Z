# adjacency Matrix
class Graph:
    def __init__(self, directed = False):
        self.graph = {}
        self.directed = directed
    
    # add node
    def add_node(self, new_node):
        self.graph[new_node] = {}
        for i in self.graph:
            self.graph[new_node][i] = 0
            self.graph[i][new_node] = 0
    # add edge
    def add_edge(self, start, end):
        self.graph[start][end] = 1
        if self.directed == False:
            self.graph[end][start] = 1

    #remove node
    def remove_node(self, node):
        self.graph.pop(node)        # remove row
        for i in self.graph:
            self.graph[i].pop(node)
    
    # remove edge
    def remove_edge(self, start, end):
        self.graph[start][end] = 0
        if self.directed == False:
            self.graph[end][start] = 0

    def __str__(self):
        ret = ""
        for k, v in self.graph.items():
            ret += f"{k}: {v}\n"
        return ret

g = Graph(True)
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 0)
g.add_edge(4, 4)
g.remove_node(3)
print(g)