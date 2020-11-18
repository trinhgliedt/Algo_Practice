# Task: generate a graph, then find all paths in the graph
from collections import defaultdict 
   
# This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self, vertices): 
        # No. of vertices 
        self.V = vertices+1
          
        # default dictionary to store graph 
        # this is an unordered collection of data values that are used to store data values like a map. 
        # self.graph = defaultdict(<class 'list'>, {})
        self.graph = defaultdict(list)  

   
    # function to add an edge to graph
    # u is the originating vertex (node), and is the key in the dict, to be paired with a list that stores the destination vertices from u
    # v is the destination vertex, stored in the list of destination vertices from u
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
    # graph = <class 'list'>, {7: [9]}
   
    # '''A recursive function to print all paths from 'u' to 'd'. 
    # visited[]: a list to keep track of vertices (nodes) in current path. 
    # path[]: a list to store actual vertices 
    def printAllPathsUtil(self, u, d, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d: 
            print(path)
        else: 
            # If current vertex is not destination 
            # Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]== False: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self, s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d, visited, path) 
   
   
   
# Create a graph given in the above diagram 
g = Graph(9) 
g.addEdge(7, 9) 
g.addEdge(6, 7) 
g.addEdge(8, 6) 
g.addEdge(8, 9) 
g.addEdge(2, 8) 
g.addEdge(1, 2) 
g.addEdge(1, 8) 
g.addEdge(5, 8) 
g.addEdge(4, 5) 
g.addEdge(3, 4) 
# graph = defaultdict(<class 'list'>, {7: [9], 6: [7], 8: [6, 9], 2: [8], 1: [2, 8], 5: [8], 4: [5], 3: [4]})
s = 1 ; d = 9
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.printAllPaths(s, d) 