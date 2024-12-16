# Mod 10 - Heaps

Implement the methods below to create a binary min-heap.

```python
class Entry:
    def __init__(self, priority, item):
        """Create a new entry for heap"""
        self.priority = priority
        self.item = item

class Heap:
    def __init__(self, entries = None):
        """Initializes heap in O(n) with optional list of Entry objects"""
        self._idx = {} # Dictionary of item:idx pairs

        if entries is not None:
            self._L = entries
            n = len(self)

            # add back half of entries to self._idx dict
            for i in range(n-1, (n-1)//2, -1):
                self._idx[self._L[i].item] = i

            # add new entries one at a time, downheaping
            for i in range((n-1)//2, -1, -1):
                self._idx[self._L[i].item] = i
                self.downheap(i)

        else:
            self._L = []

    def __len__(self):
        """Returns number of entries in heap"""
        return len(self._L)

    def i_parent(self, i):
        """Returns index of parent, or None if i is 0"""
        return (i-1)//2 if i else None
    
    def i_left(self, i):
        """Returns index of left child, or None if left child not in heap"""
        il = i*2+1
        return il if il < len(self) else None

    def i_right(self, i):
        """Returns index of right child, or None if right child not in heap"""
        ir = i*2 + 2
        return ir if ir < len(self) else None

    def i_min(self, i):
        """Returns index of min child, if such a child exists"""
        il = self.i_left(i)
        ir = self.i_right(i)
        if il is None: return None
        elif ir is None: return il

        return il if self._L[il].priority <= self._L[ir].priority else ir

    def _swap(self, i, j):
        """Swaps entries at indices i an j"""
        # Swap entries
        self._L[i], self._L[j] = self._L[j], self._L[i]
        
        # Swap indices
        item_i = self._L[i].item
        item_j = self._L[j].item
        self._idx[item_i], self._idx[item_j] = self._idx[item_j], self._idx[item_i]

    def add(self, priority, item):
        """Adds item with priority to heap"""
        self._L.append(Entry(priority, item))
        self._idx[item] = len(self)-1
        self.upheap(len(self)-1)

    def remove_min(self):
        """Removes and returns item with minimum priority"""
        # Move final item to top of heap
        self._swap(0, len(self)-1)

        # Remove min item from heap and dictionary
        item = self._L.pop().item
        self._idx.pop(item)

        # reorder heap
        self.downheap(0)

        return item

    def upheap(self, i):
        """Upheaps until heap-ordered"""
        ip = self.i_parent(i)
        while ip is not None and self._L[i].priority < self._L[ip].priority:
            self._swap(i, ip)
            i = ip
            ip = self.i_parent(i)

    def downheap(self, i):
        """Downheaps until heap-ordered"""
        imin = self.i_min(i)
        while imin and self._L[i].priority < self._L[imin].priority:
            self._swap(i, imin)
            i = imin
            imin = self.i_min(i)

    def change_priority(self, item, new_priority):
        """Updates priority of item in heap"""
        i = self._idx[item]
        self._L[i].priority = new_priority

        # Reblance heap
        self._L.upheap(i)
        self._L.downheap(i)

```