from collections import Counter as Ctr
class Graph:
    def __init__(self, directed = False):
        self.graph = dict()
        self.directed = directed
    
    # Add_Node/vertexs
    def Add_Node(self, new_node):
        if self.graph.get(new_node) is None:
            self.graph[new_node] = []
    
    # Add_Edge
    def Add_Edge(self, start, end):
        if self.graph.get(start) is None:
            self.graph[start] = []
        if self.graph.get(end) is None:
            self.graph[end] = []
        
        if self.graph.get(start) is not None:
            self.graph[start].append(end)
        
        if self.directed == False:
            if self.graph.get(end) is not None:
                self.graph[end].append(start)
    
    # remove_node
    def remove_Node(self, node):
        if self.graph.get(node) != None:
            for x in self.graph:
                if node in self.graph[x]:
                    self.graph[x].remove(node)
            del self.graph[node]     

    # remove_Edge   
    def remove_Edge(self, start, end):
        if self.graph.get(start) != None:
            if end in self.graph[start]:
                self.graph[start].remove(end)
        if self.directed == False:
            if self.graph.get(end) != None:
                if start in self.graph[end]:
                    self.graph[end].remove(start)
    
    # Print_Graph
    def Print_Graph(self):
        print("Graph: ")
        for x in self.graph:
            print(f"{x}: {self.graph[x]}")
    
    # Print_Out_Degree
    def print_Out_Degree(self):
        for x in self.graph:
            print(f"Out Degree of {x} is {len(self.graph[x])}")
    
    def print_in_Degree(self):
        marge = []
        for x in self.graph:
            marge += self.graph[x]
        in_degree = Ctr(marge)
        for x in self.graph:
            print(f"In Degree of {x} is {in_degree[x]}")


gh = Graph(True)
gh.Add_Node('A')
gh.Print_Graph()
gh.Add_Edge('A','B')
gh.Add_Edge('A','C')
gh.Add_Edge('B','C')
gh.Add_Edge('D','B')
gh.Add_Edge('C','D')
gh.Print_Graph()
gh.remove_Edge('C','D')
gh.Print_Graph()
gh.Add_Edge('A','D')
gh.Print_Graph()
gh.remove_Node('D')
gh.Print_Graph()
