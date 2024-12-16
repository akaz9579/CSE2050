class Entry:
    
    def __init__(self, priotirty, item):
        self.priotirty = priotirty
        self.item = item


class PQ_OL:
    def __init__(self):
        self._entries = []

    def insert(self, priority, item): #o(nlogn) bc if .sort. 
        self._entries.append(Entry(priority, item))
        self._entries.sort(reverse=True)  

    def find_min(self): #O(1)
        return self._entries[-1]  

    def remove_min(self): #o(1)
        return self._entries.pop()  

    def __len__(self): #o(1)
        return len(self._entries)

class PQ_UL:
    def __init__(self):
        self._entries = []

    def insert(self, priority, item): #o(1)
        self._entries.append(Entry(priority, item))
          

    def find_min(self): #o(n)
        return min(self._entries)

    def remove_min(self): #o(n)
        minVal = min(self._entries)
        self._entries.remove(minVal)
        return minVal

    def __len__(self):
        return len(self._entries)



class Node:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item
        self.left = None
        self.right = None

class PQ_BST:
    def __init__(self):
        self.root = None

    def insert(self, priority, item): #o(1)
        self._entries.append(Entry(priority, item))
          

    def find_min(self): #o(n)
        
    def remove_min(self): #o(n)

    def __len__(self):
    

class PQ_Heap:
    pass
