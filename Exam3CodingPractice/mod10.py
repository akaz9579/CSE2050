
class Entry:
    def __init__(self, priority, item):
        """Create a new entry for heap"""
        self.priority = priority
        self.item = item

class Heap:
    def __init__(self, entries = None):
        """Initializes heap in O(n) with optional list of Entry objects"""
        self.L = []
        self.idx = {} # item:index pairs

        if entries is not None:
            self.L = entries
            for i in range(len(self.L)-1,(len(self)-1)//2,-1):
                self.idx[self.L[i].item] = i
        else:
            self.L = []



    def __len__(self):
        """Returns number of entries in heap"""
        return len(self.L)
        

    def i_parent(self, i):
        """Returns index of parent, or None if i is 0"""
        i = (i-2)//2
        if i<=0:return None
        else: return i
        
    
    def i_left(self, i):
        """Returns index of left child, or None if left child not in heap"""
        i = 2*i+1
        if i > len(self.L)-1:
            return None
        else: return i
        


    def i_right(self, i):
        """Returns index of right child, or None if right child not in heap"""
        i = 2*i+1
        if i > len(self.L)-1:
            return None
        else: return i
        





    def _swap(self, i, j):
        """Swaps entries at indices i an j"""
        self.L[i], self.L[j] = self.L[j], self.L[i]

        self.idx[self.L[i].item], self.idx[self.L[j].item] =  self.idx[self.L[j].item], self.idx[self.L[i].item]

        


    def add(self, priority, item):
        """Adds item with priority to heap"""
        self.L.append(Entry(priority, item))
        self.idx[item] = len(self.L)-1
        self.upheap(len(self))
        




    def remove_min(self):
        """Removes and returns item with minimum priority"""
        min = self.L[0]
        self._swap(0,len(self)-1)
        self.L.pop()
        self.idx.pop(min)
        self.downheap(0)
        return min.item
    

    
    def i_min(self, i):
        """Returns index of min child, if such a child exists"""
        indexLeft = self.i_left(i)
        indexRight = self.i_right
        if indexLeft is None:return None
        if indexRight is None: return indexLeft
        
        #check priority:
        if self.L[indexLeft].priority <= self.L[indexRight].priority:
            return indexLeft
        else: return indexRight

    def downheap(self, i):
        """Downheaps until heap-ordered"""
        minChild = self.i_min
        while minChild and self.L[minChild].priority < self.L[i].priority:
            self._swap(i, minChild)
            i , minChild = minChild, i

        


    def upheap(self, i):
        """Upheaps until heap-ordered"""
        parentIndex =  self.i_parent(i)
        leftIndex = self.i_left(i)
        rightIndex =  self.i_right(i)

        while parentIndex and self.L[i].priority < self.L[parentIndex].priority:
            self._swap(i, parentIndex)
            i, parentIndex = parentIndex,i





    def change_priority(self, item, new_priority):
        """Updates priority of item in heap"""
        index = self.idx[item]

        self.upheap(index)
        self.downheap(index)

        




        
