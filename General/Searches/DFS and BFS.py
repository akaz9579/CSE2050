from Graph import Graph_ES
from Graph import Graph_AS

class Graph(Graph_AS):
    #recursive, using a list 
#    def dfs_r(self,v):
#       path = [v]
#    
#    def _dfs_r(self,v,path):
#        for n in self.neighbors(v):
#            if n not in path:
#                path.append(n)
#                return self._dfs_r(n,path)
#        return path
#

    #recursive, using a tree
    def dfs_r(self,v):
       tree = {v:None} # child:parent
       return self._dfs_r(v,tree)
    
    def _dfs_r(self,v,tree):
        for n in self.neighbors(v):
            if n not in tree:
                tree[n] = v
                return self._dfs_r(n,tree)
        return tree
    
    #iterative
    def dfs_iter(self,v):
        tree = {}
        to_visit = [(None, v)]

        while to_visit:
            parent, child = to_visit.pop()
            if child not in tree:
                tree[child] = parent
                for n in self.neighbors(child):
                    to_visit.append((child, n))
        
        return tree
    
    def bfs(self, v):
        tree = {} 
        to_visit = [(None,v)]

        while to_visit:
            a,b = to_visit.pop(0)
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    to_visit.append((b,n))

            return tree
        

    
    
    
    





if __name__ == '__main__':
    g = Graph()
# 1--4--6
# |\ | /|
# | \|/ |
# 2--3--5 
    vs = {1,2,3,4}
    es = {(1,2),(1,3),(1,4),
          (2,1),(2,3),
          (3,1),(3,2),(3,4),(3,5), (3,6),
          (4,1),(4,3), (4,6),
          (5,3),(5,6),
          (6,3), (6,4),(6,5)}
    
    
    for v in vs:
        g.add_vertex(v)
    for e in es:
        g.add_edge(e)

    print(f"dfs(4) = {g.dfs_r(4)}")
    print(f"dfs(4) = {g.dfs_iter(4)}")

 