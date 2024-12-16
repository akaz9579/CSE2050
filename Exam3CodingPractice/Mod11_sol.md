# Mod 11 - Graphs

Implement the methods below to create an undirected, unweighted, simple graph.

```python
class Graph:
    def __init__(self, V=None, E=None):
        """Initializes a graph with optional sets of vertices V and edges E"""
        self._nbrs = {}

        if V is not None:
            for v in V:
                self.add_vertex(v)
            
        if E is not None:
            for e in E:
                self.add_edge(e)
        
    def add_vertex(self, v):
        """Adds vertex v to graph"""
        self._nbrs.setdefault(v, set())

    def add_edge(self, e):
        """Addes edge e to graph"""
        # Add in both directions for undirected graph
        self._nbrs[e[0]].add(e[1])
        self._nbrs[e[1]].add(e[0])

    def neighbors(self, v):
        """Returns iterator of neighbors of v"""
        return iter(self._nbrs[v])

    def __iter__(self):
        """Iterates over all vertices in graph"""
        return iter(self._nbrs)

    def is_connected(self, v1, v2):
        """Returns True (False) if v1 and v2 are (are not) connected"""
        return self._is_connected(v1, v2, set())

    def _is_connected(self, v1, v2, visited):
        """Helper function for is_connected"""
        if v1 in visited: return False
        if v1 == v2: return True
        visited.add(v1)
        return any(self._is_connected(nbr, v2, visited) for nbr in self.nbrs(v1))

    def dfs_recr(self, v):
        """Recursive Depth-first search starting at v"""
        tree = {v:None}
        _dfs(v, tree)
        return tree

    def _dfs(self, v, tree):
        """Helper function for _dfs_recr"""
        for u in self.neighbors(v):
            if u not in tree:
                tree[u] = v
                self._dfs(u, tree)

    def dfs(self, v):
        """Depth-first search starting at v"""
        tree = dict()
        to_visit = []
        to_visit.append((None, v))

        while not to_visit.empty():
            a, b = to_visit.pop()
            if not b in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    to_visit.append((b, n))

        return tree

    def bfs(self, v):
        """Breadth-first search starting at v"""
        tree = dict()
        to_visit = Queue()
        to_visit.put((None, v))

        while not to_visit.empty():
            a, b = to_visit.get()
            if not b in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    to_visit.put((b, n))

        return tree  
```