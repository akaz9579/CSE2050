class Deque:
    def __init__(self):                                 # O(1)
        """Initializes an empty deque"""
        self._L = []
        
    def add_first(self, item):                          # O(n)
        """Adds item to "front" of deque"""
        self._L.append(item)
        

    def add_last(self, item):                           # O(1)
        """Adds item to "end" of deque"""
        
    def remove_first(self):                             # O(n)
        """Removes and returns first item in deque"""
        return 
    
    def remove_last(self):                              # O(1)
        """Removes and returns last item in deque"""
        return 

    def __len__(self):                                  # O(1)
        """Returns number of items in deque"""
        return 

    def is_empty(self):                                 # O(1)
        """Returns True iff deque is empty"""
        return 