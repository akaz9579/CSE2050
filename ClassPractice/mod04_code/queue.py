class Queue:
    def __init__(self):
        """Initializes an empty queue"""
        self._L = [] # List "wrapper"

    def __len__(self):
        """Returns the number of items in the queue"""
        return len(self._L)
    
    def enqueue(self, item):
        """Adds item to end of queue"""
        self._L.insert(0, item) # O(n)

    def dequeue(self):
        """Removes and returns first item in queue"""
        return self._L.pop() # O(1)
    
    def peek(self):
        """Returns (but does not remove) next item in queue"""
        return self._L[-1]
    
    def is_empty(self):
        """Returns True iff queue is empty"""
        return len(self) == 0