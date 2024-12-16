
class Graph:
    def __init__(self, V=None, E=None):
        """Initializes a graph with optional sets of vertices V and edges E"""
        self.vertices = set()
        self.edge = set()
        self.nbrs = {}
        
        if V is not None:
            for vert in V:
                self.add_vertex(vert)
        if E is not None:
            for edge in E:
                self.add_edge(edge)

    def add_vertex(self, v):
        """Adds vertex v to graph"""
        self.vertices.add(v)
        
        if v not in self.nbrs:
            self.nbrs[v] = set()


        

    def add_edge(self, e):
        """Addes edge e to graph"""
        self.edge.add(e)
        # Add in both directions for undirected graph

        v,u = e
        self.edge.add((u,v)) 

        if v not in self.nbrs:
            self.nbrs[v] = set()
        if u not in self.nbrs:
            self.nbrs[u] = set
        self.nbrs[v].add(u)
        self.nbrs[u].add(v)
        
    


    def neighbors(self, v):
        """Returns iterator of neighbors of v"""
        return iter(self.nbrs[v])

    
        

    def __iter__(self):
        """Iterates over all vertices in graph"""
        return iter(self.vertices)
    


    def is_connected(self, v1, v2):
        """Returns True (False) if v1 and v2 are (are not) connected"""
        if v1 in self.nbrs[v2] or v2 in self.nbrs[v1]:
            return True
        else:
            return self._is_connected(v1,v2,set())
        
    
    def _is_connected(self,v1,v2,visited):
        """"""
        if v1 in visited:
            return False
        if v1 == v2:
            return True
        visited.add(v1)

        for nbrs in self.nbrs[v1]:
            return self._is_connected(nbrs,v2,visited)
        
    def dfs_recr(self, v):
        """Recursive Depth-first search starting at v"""
        tree = {None:v}
        return self._dfs_recursive(v,tree)
 
    def _dfs_recursive(self,v,tree):
        """"""
        for nbr in self.nbrs[v]:
            tree[v] = nbr
            self._dfs_recursive(nbr,tree)
        return tree
    
    def dfs_iter(self,v):
        """"""
        tree = {}
        toVisit = [(None, v)]

        while toVisit:
            a,b = toVisit.pop()
            if b not in tree:
                    tree[b] = a
                    for nbrs in self.nbrs[b]:
                        toVisit.append((b,nbrs))
        return tree

    
    def bfs(self, v):
        """Breadth-first search starting at v"""
        tree = {}
        toVisit = [(None, v)]

        while toVisit:
            a,b = toVisit.pop(0)
            if b not in tree:
                tree[b] =a
                for nbrs in self.nbrs[b]:
                    toVisit.append((b,nbrs))
        return tree




    def yes(self,v,tree = {}):
        for nbrs in self.nbrs[v]:
            tree[v] = nbrs
            self.yes(nbrs,tree)
        return tree





        
