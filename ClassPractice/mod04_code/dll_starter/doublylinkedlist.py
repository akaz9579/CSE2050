###############################################################################
# WARMUP: Get as much doubly linked list done as you can.                     #
# Starter code in slides_scoggin > mod04_code > dll_starter                   #
# Tests are there as well.                                                    #
###############################################################################

class Node:
    def __init__(self, data, prev=None, link=None):
        """Initializes a new node"""
        self.data = data
        self.prev = prev
        self.link = link
        

    def __repr__(self):
        return f"Node({self.data})"
    
class DoublyLinkedList:
    def __init__(self, items=None):
        self._head = None
        self._tail = None 
        self._len = 0

        if items is not None:
            for item in items:
             self.add_last(item)
    

    def __len__(self):
        return self._len
    
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail 
    
    def add_first(self, data):
        if len(self)==0:
            self._head = Node(data)
            self._tail= self._head
        else:
            n1= Node(data, prev=None,link=self._head)
            self._head.prev = n1
            self._head = n1
       
        self._len +=1
        

    def add_last(self, data):
        if len(self)==0:
            self._head = Node(data)
            self._tail= self._head
        else:
            n1 = Node(data,self._tail, None)
            self._tail.link = n1
            self._tail = n1
        self._len +=1


    
    def remove_first(self):
        oldhead = self._head.data
        if len(self) == 1:
            self._head = self._tail = None
        else: 
            self._head = self._head.link 
            self._head.prev = None
        self._len -=1
        return oldhead 
    

    def remove_last(self):
        oldtail = self._tail.data
        if len(self) == 1:
            self._head = self._tail = None
        else: 
            self._tail = self._tail.prev
            self._tail.link = None
        self._len -=1
        return oldtail 
    