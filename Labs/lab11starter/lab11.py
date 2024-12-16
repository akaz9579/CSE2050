class Graph_ES:
    def __init__(self, Vs, Es):
        self.vs = Vs
        self.Es = Es 
    
    def add_vertex(self,v):
        self.vs.add(v)
    
    def add_edge(self,e):
        self.Es.add(e)

    def remove_vertex(self, v):
        self.vs.remove(v)

    def remove_edge(self, e):
        self.Es.remove(e)

    def __iter__(self):
        return iter(self.vs)
    
    def _neighbors(self,v):
        nb = set()
        
        for e in self.Es:
            if e[0] == v:
                nb.add(e[1])

        return nb
    
    def __len__(self):
        return len(self.vs) 



class Graph_AS:
    def __init__(self, Vs, nb):
        self.vs = Vs
        self.nb = dict()
        
        for i in nb:
            self.add_edge(i)


    
    def add_vertex(self,v):
        self.vs.add(v)
    
    def add_edge(self,e):
        a,b = e

        if a not in self.nb:
            self.nb[a] = {b}
        else:
            self.nb[a].add(b)

    def remove_vertex(self, v):
        self.vs.remove(v)

    def remove_edge(self, e):
        a,b = e
        self.nb[a].remove(b)
        if len(self.nb[a]) ==0:
            self.nb.pop(a)

    def __iter__(self):
        return iter(self.vs)
    
    def _neighbors(self,v):       
        return iter(self.nb[v])
    
    def __len__(self):
        return len(self.vs) 
    
    

