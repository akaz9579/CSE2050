class Entry:
    def __init__(self, priority, value):
        """Instantiates a new entry object"""
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        """Entries are compared based on priority"""
        return self.priority < other.priority
    
    def __le__(self, other):
        return self < other or self == other
    
    def __eq__(self, other):
        """Entries are equal if they have the same priority"""
        return self.priority == other.priority

    def __repr__(self):
        """Returns string representation of Entry"""
        return f"Entry({self.priority}, {self.value})"
    
class minHeap:
    def __init__(self):
        """Instantiates a new, empty heap"""
        self._L = []

    def __len__(self):
        """Returns number of entries in heap"""
        return len(self._L)
    
    def add(self, item, priority):
        """Adds item w/ given priority to heap"""
        self._L.append(Entry(priority=priority, value=item))
        self._upheap(idx=len(self)-1)

    def remove_min(self):
        """Removes and returns entry with minimum priority"""
        # Extract the item to return
        item = self._L[0]

        # Move last item to top of heap
        self._swap(0, len(self)-1)
        self._L.pop()

        # Re-order heap
        self._downheap(idx=0)

        return item

    def _upheap(self, idx):
        """Upheaps item at idx until heap is heap-ordered"""
        # Find parent index
        # Swap until I am heap-ordered
        i_p = self._parent(idx) # get the index of the parent

        while i_p is not None and self._L[idx] < self._L[i_p]:
            # self._L[idx], self._L[i_p] = self._L[i_p], self._L[idx]
            self._swap(idx, i_p) # swap entries at these 2 indices
            idx = i_p
            i_p = self._parent(idx)
            
        # Implement self._parent() and self._swap

    def _downheap(self, idx):
        """Downheaps item at idx until heap is heap-ordered"""
        i_min = self._min_child(idx)

        while i_min is not None and self._L[idx] > self._L[i_min]:
            self._swap(idx, i_min)
            idx = i_min
            i_min = self._min_child(idx)

    def _parent(self, idx):
        """Returns index of parent"""
        i_p = (idx - 1) // 2 # 1 -> 0; 2 -> 0
        return i_p if idx else None

    def _left(self, idx):
        """Returns index of left child or None"""
        i_l = 2*idx + 1
        return i_l if i_l < len(self) else None

    def _right(self, idx):
        """Returns index of right child or None"""
        i_r = 2*idx + 2
        return i_r if i_r < len(self) else None

    def _min_child(self, idx):
        """Returns index of minimum child or None"""
        i_l, i_r = self._left(idx), self._right(idx)
        
        if i_l is None: return None # no children
        elif i_r is None: return i_l # one child
        else: return i_l if self._L[i_l] <= self._L[i_r] else i_r 

    def _swap(self, i, j):
        """Swaps items at given indices in heap"""
        self._L[i], self._L[j] = self._L[j], self._L[i]

    def __iter__(self):
        """Iteratively removes every item in heap"""
        while self: # true unless len(self) == 0
            yield self.remove_min()

if __name__ == '__main__':
    # Insert priorities from 0 to 6
    priorities = list(range(7))  # [0, 1, 2, 3, 4, 5, 6]
    
    # Initialize heap
    h = minHeap()

    # Insert elements into the heap
    for priority in priorities:
        h.add(item=priority, priority=priority)  # Use the same value for item and priority

    # Print heap state after insertion
    print("Heap after insertion:", [(entry.priority, entry.value) for entry in h._L])

    # Remove the minimum element and print the heap state
    h.remove_min()
    print("Heap after removing min:", [(entry.priority, entry.value) for entry in h._L])

    # Remove all remaining elements to observe heap behavior
    while len(h) > 0:
        print("Removing min:", h.remove_min())
        print("Current heap state:", [(entry.priority, entry.value) for entry in h._L])