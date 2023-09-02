# Graph is two type 
# 1. Directed
# 2. Undirected

class Graph:
    def __init__(self, directed = False):
        self.graph = dict()
        self.directed = directed

    def add_Node(self, new_Node):
        if self.graph.get(new_Node) is None:
            self.graph[new_Node] = []
    
    def add_Edge(self, start, end):
        if self.graph.get(end) is None:
            self.graph[end] = []

        if self.graph.get(start) is not None:
            self.graph[start].append(end)
        
        if self.directed == False:
            if self.graph.get(end) is not None:
                self.graph[end].append(start)
        
        def remove_Node(self, node):
            if self.graph.get(node) is not None:
                for x in graph:
                    if node in self.

        def remove_Edge(self, start, end):
            if self.graph.get(start) is not None:
                if end in self.graph[start]:
                    self.graph[start].remove(end)
            if self.directed == False:
                if self.graph.get(end) is not None:
                    if start in self.graph[end]:
                        self.graph[end].remove(start)

        

    def print_Graph(self):
        print("Graph\n")
        for x in self.graph:
            print(x, ":", slef.graph[x])

    def print_OutDegree(self):
        for x in self.graph:
            print("Out Degree of ", x , "is ", len(self.graph[x]))
    
    
    def print_InDegree(self):
        merge = []
        for x in self.graph:
            merge+ = self.graph[x]
        indegree = Counter(merge)
        for x in self.graph:
            print("In Degree is ", indegree)


    # Question_01
    def findMaxInOutDegree(self):
        maxin = -1
        maxout = -1
        maxInList = []
        maxOutList = []

        merge = []
        for x in self.graph:
            merge += graph[x]
            
