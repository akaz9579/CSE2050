class Stack:
    def __init__(self):
        """Initializes an empty stack"""
        self._stack = []


    def push(self, item): 
        """Adds item to top of stack"""
        return self._stack.append(item)


    def pop(self):
        """Removes and returns top item from stack"""
        return self._stack.pop()

    
    def peek(self):
        """Returns (but does not remove) top item"""
        return self._stack[-1]

    
    def __len__(self): # O(1)
        """Returns number of items in stack"""
        return len(self._stack)

    
    def is_empty(self): # O(1)
        """Returns True iff stack is empty"""
        return len(self) == 0

        