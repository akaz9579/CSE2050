# mapping/mapping.py
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Entry({self.key},{self.value})"
    def __str__(self):
        return str(self.key) + " : " + str(self.value)
    
def mapput(L, key, value):
    for e in L:
        if e.key == key:
            e.value = value
            return
    L.append(Entry(key, value))

def mapget(L, key):
    for e in L:
        if e.key == key:
            return e.value
    raise KeyError

m = []
mapput(m, 4, 'five')
mapput(m, 1, 'one')
mapput(m, 13, 'thirteen')
mapput(m, 4, 'four')
assert(mapget(m, 1) == 'one')
assert(mapget(m, 4) == 'four')