

class Node:
    def __init__(self, item, link = None):
        """Creates node with data and link """

        self.item = item
        self.link = link

    def __repr__(self):
        """"""
        return f"Node({self.item})"

class LinkedList:
    def __init__(self, item = None):
        """Creates a linked list with ability to add and remove from head and the tail"""

        self._head = None
        self._tail = None
        self._len = 0

        if item is not None:
            for x in item:
                self.add_last(x)


    def __repr__(self):
        """"""
        return f"Node({self._head})"
    def __len__(self):
        """"""
        return self._len
    def get_head(self):
        """"""
        if self._head is None:
            return None
        else:
            return self._head.item
    def get_tail(self):
        """"""
        if self._tail is None:
            return None
        else:
            return self._tail.item
    
    def add_last(self,item):
        """"""
        n1= Node(item)

        if self._tail is None:
            self._tail = n1
            self._head = n1
        else:
            self._tail.link = n1
            self._tail = n1
        
        self._len +=1

    def add_first(self, item):
        """"""
        n1 = Node(item, self._head)

        if self._head is None:  
            self._tail = n1
        self._head = n1
        self._len += 1

    def remove_last(self):
        """"""
        if self._head is None:
            raise RuntimeError("Can't remove from empty list")
        if self._head == self._tail:  
            old_tail = self._tail.item
            self._head = None
            self._tail = None
        else:  
            current = self._head
            while current.link != self._tail:
                current = current.link
            old_tail = self._tail.item
            self._tail = current
            self._tail.link = None

        self._len -= 1
        return old_tail
    
    def remove_first(self):
        """"""
        if self._head is None:  #
            raise RuntimeError("Cannot remove from an empty list")  # Raise an error if empty

        old_head = self._head.item
        self._head = self._head.link
        if self._head is None: 
            self._tail = None
        self._len -= 1
        return old_head




    
    

    
  
        
    
    
