class Node:
    def __init__(self, data, link=None):
        """Initializes a new node"""
        self.data = data
        self.link = link

    def __repr__(self):
        return f"Node({self.data})"

class LinkedListTail:
   
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
        self._head = Node(item, self._head)
        if self._len == 0: self._tail = self._head
        self._len +=1 


    def add_last(self, item):
        "Adds a new node at the end and updates tail"
        new_node = Node(item)
        if self._len == 0:  
            self._head = self._tail = new_node
        else:  
            self._tail.link = new_node
            self._tail = new_node
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
            self._head = self._head.link
            oldhead.link = None
        self._len -= 1
        return oldhead.data

    def remove_last(self):
        "finds last item and removes. returns old tail"
        if self._len == 0:
            return None
        elif self._len == 1:
            oldtail = self._tail
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.link.link is not None:
                current = current.link
            oldtail = current.link
            current.link = None
        self._len -= 1
        return oldtail.data
    