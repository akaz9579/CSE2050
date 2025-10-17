class Node:
    def __init__(self, data, next=None, prev = None):
        """Initializes a new node"""
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node({self.data})"

class DLL:
   
    def __init__(self):
        self._head = None 
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len
    
    def get_head(self):
        return self._head.data

    def get_tail(self):
        return self._tail.data
    

    def add_first(self, item):
        "sets head to new node and links to old"
        self._head = Node(item, self._head, None)
        if self._len == 0: self._tail = self._head
        self._len +=1 


    def add_last(self, item):
        "Adds a new node at the end and updates tail"
        new_node = Node(item,None, self._tail)
        if self._len == 0:  
            self._head = self._tail = new_node
        else:  
            self._tail.next = new_node
            self._tail = self._tail.next
        self._len += 1

    def remove_first(self):
        "finds first item and removes. returns old head"

        if self._len == 0:
            return None
        elif self._len == 1:
            oldhead = self._head
            self._head = None
            self._tail = None
        else:
            oldhead = self._head
            self._head = self._head.next
            self._head.prev = None
            oldhead.next = None
        self._len -= 1
        return oldhead.data

    def remove_last(self):
        "finds last item and removes. returns old tail"
        if self._len == 0:
            return None
        elif self._len == 1:
            oldtail = self._tail
            self._head = self._tail = None
        else:
            oldtail = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            oldtail.prev = None
        self._len -= 1
        return oldtail.data
    