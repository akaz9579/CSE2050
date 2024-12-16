from entry import Entry

class Heap:
    def __init__(self):
        """New empty heap"""
        self._L = []
        self._idx = {}  

    def __len__(self):
        """Returns number of entries in heap"""
        return len(self._L)

    def __iter__(self):
        """Iterate through entries yielding min until heap is empty."""
        while self._L:
            yield self.remove_min()

    def _parent(self, idx):
        """Returns index of parent"""
        return (idx - 1) // 2 if idx else None

    def idx_parent(self, idx):  
        """Returns the index of the parent"""
        return self._parent(idx)

    def idx_left(self, idx):
        """Returns index of left child or None"""
        i_l = 2 * idx + 1
        return i_l if i_l < len(self) else None
    
    def idx_right(self, idx):
        """Returns index of right child or None"""
        i_r = 2 * idx + 2
        return i_r if i_r < len(self) else None
    
    def idx_min_child(self, idx):
        """Returns index of minimum child or None"""
        idx_left, idx_right = self.idx_left(idx), self.idx_right(idx)
        if idx_left is None:
            return None
        elif idx_right is None:
            return idx_left
        else:
            return idx_left if self._L[idx_left] <= self._L[idx_right] else idx_right

    def insert(self, item, priority):
        """Adds item with given priority to heap"""
        entry = Entry(item=item, priority=priority)
        self._L.append(entry)
        self._idx[item] = len(self) - 1
        self._upheap(len(self) - 1)

    def remove_min(self):
        """Removes and returns entry with min priority"""
        if not self._L:
            return None  
        entry = self._L[0]
        last_item = self._L.pop()  
        if self._L:
            self._L[0] = last_item  
            self._idx[last_item.item] = 0
            self._downheap(0)
        del self._idx[entry.item]  
        return entry

    def change_priority(self, item, priority):
        """Change the priority of a given item."""
        idx = self._idx.get(item)
        if idx is not None:
            self._L[idx].priority = priority
            self._upheap(idx)  
            self._downheap(idx)  
            return self._idx[item]  
        return None

    def _swap(self, i, j):
        """Swaps items at given indices in heap"""
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """Upheaps item at idx until heap is heap-ordered"""
        while idx > 0:
            i_p = self._parent(idx)
            if self._L[idx] < self._L[i_p]:
                self._swap(idx, i_p)
                idx = i_p
            else:
                break

    def _downheap(self, idx):
        """Downheaps item at idx until heap is heap-ordered"""
        while True:
            idx_min = self.idx_min_child(idx)
            if idx_min is None or self._L[idx] <= self._L[idx_min]:
                break
            self._swap(idx, idx_min)
            idx = idx_min

    @staticmethod
    def heapify(entries):
        """Create and return a heap out of the passed list of Entry objects."""
        heap = Heap()
        heap._L = list(entries)
        for i in reversed(range(len(heap._L) // 2)):
            heap._downheap(i)
        heap._idx = {entry.item: i for i, entry in enumerate(heap._L)}
        return heap
