
class Graph:
    def __init__(self, V=None, E=None):
        """Initializes a graph with optional sets of vertices V and edges E"""
        self.vertices = set()
        self.edges = set()
        self.nbrs = dict()

        if V is not None:
            for i in V:
                self.add_vertex(i)
        if E is not None:
            for i in E:
                self.add_edge(i)

        
    def add_vertex(self, v):
        """Adds vertex v to graph"""
        self.vertices.add(v)

        if v not in self.nbrs:
            self.nbrs[v] = set()
        else:
            

        

    def add_edge(self, e):
        """Addes edge e to graph"""
        self.edges.add(e)
        # Add in both directions for undirected graph

        v, u = e
        self.edges.add((u,v)) 

        if v not in self.nbrs:
            self.nbrs[v] = set()
        else:
            self.nbrs[v].add(u)

    



    def neighbors(self, v):
        """Returns iterator of neighbors of v"""
        return iter(self.nbrs)
    
        

    def __iter__(self):
        """Iterates over all vertices in graph"""
        return iter(self.vertices)

    def is_connected(self, v1, v2):
        """Returns True (False) if v1 and v2 are (are not) connected"""
        if v2 in self.nbrs[v1] or v1 in self.nbrs[v2]:
            return True
        if v2 in self.dfs_iter(v1): return True
        else: return False



    def dfs_recr(self, v):
        """Recursive Depth-first search starting at v"""
        tree = {None:v}
        self._dfs_recursive(v,tree)
        return tree
    
    def _dfs_recursive(self,v,tree):
        for nbr in self.nbrs[v]:
            tree[v] = nbr
            return self._dfs_recursive(v,tree)
  


    def dfs_iter(self,v):
        tree = {} # child parent
        toVisit = [(None, v)]

        while toVisit:
            a,b = toVisit.pop()
            if b not in tree:
                tree[b]= a
                for nbrs in self.nbrs[b]:
                    toVisit.append((b,nbrs))

        return tree           


    def bfs(self, v):
        """Breadth-first search starting at v"""
        tree = dict()
        toVisit = [(None,v)]

        while toVisit:
            a,b = toVisit.pop(0)
            if b not in tree:
                tree[b] = a
                for nbrs in self.nbrs[b]:
                    toVisit.append((b,nbrs))
        return tree










        
