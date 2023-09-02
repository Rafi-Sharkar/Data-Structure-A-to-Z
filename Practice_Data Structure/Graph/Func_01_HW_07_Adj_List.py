# adjacency List
from collections import Counter
class Graph:
    def __init__(self, directed = False):
        self.graph = {}
        self.directed = directed
    
    # add Node
    def add_Node(self, new_node):
        if self.graph.get(new_node) is None:
            self.graph[new_node] = []

    # add Edge
    def add_Edge(self, start, end):
        if self.graph.get(start) is None:
            self.graph[start] = []
        if self.graph.get(end) is None:
            self.graph[end] = []
        
        if self.graph.get(start) is not None:
            self.graph[start].append(end)
        if self.directed == False:
            if self.graph.get(end) is not None:
                self.graph[end].append(start)
    
    # remove node
    def remove_node(self, node):
        if self.graph[node] != None:
            for i in self.graph:
                if node in self.graph[i]:
                    self.graph[i].remove(node)
            del self.graph[node]
        
    # remove Edge
    def remove_edge(self, start, end):
        if self.graph[start] != None:
            if end in self.graph[start]:
                self.graph[start].remove(end)
        
        if self.directed == False:
            if self.graph[end] != None:
                if start in self.graph[end]:
                    self.graph[end].remove(start)

# Question_01
    # find_Max_In_Out_Degree
    def find_Max_In_Out_Degree(self):
        max_in = -1
        max_out = -1
        max_in_list = []
        max_out_list = []
    
        marge = []
        for x in self.graph:
            marge += self.graph[x]
        in_degree = Counter(marge)
        for x in in_degree:
            if in_degree[x] >= max_in:
                max_in = in_degree[x]
        for x in in_degree:
            if in_degree[x] == max_in:
                max_in_list.append(x)
        
        print(f"Max In Degree Nodes: {max_in_list}")

        for x in self.graph:
            if len(self.graph[x]) >= max_out:
                max_out = len(self.graph[x])
        for x in self.graph:
            if len(self.graph[x]) == max_out:
                max_out_list.append(x)
        print(f"Max Out Degree Nodes: {max_out_list}")

# Question_02
    # Find_Common_Adjacency_Node
    def Find_Common_Adjacency_Node(self, node1, node2):
        common_adj_node = []
        for i in len(self.graph[node1]):
            for j in len(self.graph[node2]):
                if i == j:
                    common_adj_node.append(i)


# Question_03
    # Print_Sink_Node
    def Print_Sink_Node(self):
        sink_node = []
        for x in self.graph:
            if len(self.graph[x]) == 0:
                sink_node.append(x)
        print("Sink Node: ",sink_node)

    # print
    def Print_Graph(self):
        print("Graph: ")
        for i in self.graph:
            print(f"{i}: {self.graph[i]}")
        

g = Graph()
g.add_Node(0)
g.add_Node(1)
g.add_Node(2)
g.add_Node(3)
g.add_Node(4)
g.add_Edge(1, 0)
g.add_Edge(0, 2)
g.add_Edge(0, 3)
g.add_Edge(2, 3)
g.add_Edge(3, 4)
g.add_Edge(4, 4)
g.Print_Graph()
# g.find_Max_In_Out_Degree()




