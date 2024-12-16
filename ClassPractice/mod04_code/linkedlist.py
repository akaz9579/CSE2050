class Node:
    def __init__(self, data, link=None):
        """Initializes a new node"""
        self.data = data
        self.link = link

    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
   
    def __init__(self, items):
        
        self._head = None 
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len
    
    def add_first(self, item):
        oldHead = 
        self._head = Node(item, self._head)
        self._len += 1 

    def add_last(self, item):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def get_head(self):
        pass

    def get_tail(self):
        node = self._head

        while node.link is not None:
            node = node.link 
        return node 
    