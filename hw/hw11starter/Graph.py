class Graph:
    def __init__(self, V=None, E=None):
        raise NotImplementedError("Use AdjacencySetGraph or EdgeSetGraph.")

    def is_connected(self, v1, v2):
        """Check if two vertices are connected using BFS."""
        visited = self.bfs(v1)
        return v2 in visited

    def bfs(self, v):
        """Perform BFS and return a tree as a dictionary."""
        tree = {}
        queue = [(None, v)]
        visited = set()

        while queue:
            parent, current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                tree[current] = parent
                for neighbor in self.nbrs(current):
                    if neighbor not in visited:
                        queue.append((current, neighbor))
        return tree

    def shortest_path(self, v1, v2):
        """Return the shortest path between two vertices."""
        bfs_tree = self.bfs(v1)
        if v2 not in bfs_tree:
            return None
        path = []
        current = v2
        while current is not None:
            path.insert(0, current)
            current = bfs_tree[current]
        return path

    def count_trees(self):
        """Count and return all trees in the graph."""
        visited = set()
        trees = []
        for vertex in self:
            if vertex not in visited:
                tree = self.bfs(vertex)
                trees.append(tree)
                visited.update(tree.keys())
        return trees, len(trees)

    def nbrs(self, v):
        """Abstract method to return neighbors of a vertex."""
        raise NotImplementedError("Subclasses must implement this method.")


class AdjacencySetGraph(Graph):
    def __init__(self, V=None, E=None):
        self.vertices = set()
        self.adjacency = {}

        if V:
            for vertex in V:
                self.add_vertex(vertex)
        if E:
            for edge in E:
                self.add_edge(edge)

    def add_vertex(self, v):
        if v not in self.adjacency:
            self.adjacency[v] = set()
        self.vertices.add(v)

    def add_edge(self, e):
        u, v = e
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Vertices must exist in the graph.")
        if v not in self.adjacency[u]:
            self.adjacency[u].add(v)
        if u not in self.adjacency[v]:
            self.adjacency[v].add(u)

    def nbrs(self, v):
        return iter(self.adjacency.get(v, set()))

    def __iter__(self):
        return iter(self.vertices)


class EdgeSetGraph(Graph):
    def __init__(self, V=None, E=None):
        self.vertices = set()
        self.edges = set()

        if V:
            for vertex in V:
                self.add_vertex(vertex)
        if E:
            for edge in E:
                self.add_edge(edge)

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, e):
        u, v = e
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Vertices must exist in the graph.")
        if (u, v) not in self.edges and (v, u) not in self.edges:
            self.edges.add((u, v))

    def nbrs(self, v):
        return {u if u != v else w for u, w in self.edges if v in (u, w)}

    def __iter__(self):
        return iter(self.vertices)