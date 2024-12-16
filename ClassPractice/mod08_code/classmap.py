class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Entry({self.key},{self.value})"
    def __str__(self):
        return str(self.key) + " : " + str(self.value)
class Mapping:
    def __init__(self):
        self._L = []

    def __setitem__(self,key,value):
        for entry in self._L:
            if entry.key ==key:
                entry.value = value
                return
        
        self._L.append(Entry(key,value))
            

    def __getitem__(self,key):
        for entry in self._L:
            if entry.key == key:
                return entry.value
                    
        raise KeyError
    

class Mapping2:
    def __init__(self):
        self._L = []

    def __setitem__(self,key,value):
        for entry in self._L:
            if entry.key ==key:
                entry.value = value
                return
        
        self._L.append(Entry(key,value))
            

    def __getitem__(self,key):
        n= len(self._L)
        for i in range(n):
            if self._L[n-1-i].key == key:
                return self.[n-1-i].value
        
                    
        raise KeyError
        


if __name__ == '__main__':
    m1= Mapping()
    m1['jake']
