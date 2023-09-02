class Graph:
    def __init__(self):
        self.graph = {}
    
    # Add Node
    def Add_Node(self, new_node):
        self.graph[new_node] = {}
        for i in self.graph:
            self.graph[new_node][i] = 0     # add a new row
            self.graph[i][new_node] = 0     # add a new column
        
    # Add Edge
    def Add_Edge(self, start, end):
        self.graph[start][end] = 1
        self.graph[end][start] = 1
    
    # remove node
    def remove_Node(self, node):
        # remove row
        self.graph.pop(node)
        # remove column
        for i in self.graph:
            self.graph[i].pop(node)

    # remove Edge
    def remove_Edge(self, start, end):
        self.graph[start][end] = 0
        self.graph[end][start] = 0
    
    # print
    def __str__(self):
        ret = ""
        for k, v in self.graph.items():
            ret += f"{k}: {v}\n"
        return ret

g = Graph()
g.Add_Node(1)
g.Add_Node(2)
g.Add_Node(3)
g.Add_Node(4)
print(g)
g.remove_Node(3)
print(g)

    
