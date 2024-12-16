
class Node:
    def __init__(self, key, value):
        """Creates a new node with key and value"""
        self.key = key
        self.value = value
        self.height = 0 
        self.left = None
        self.right = None


    def update_height(self):
        """Updates height of this node"""
        if self.left is not None: heightLeft = self.left.height
        else: heightLeft = -1

        if self.right is not None: heightRight = self.right.height
        else: heightRight = -1
        self.height = max(heightLeft, heightRight) +1


    def put(self, key, value):
        """Adds key:value pair, or updates value if key already in mapping"""
        if self.key == self.value:
            self.value = value 
        if key < self.key:
            if self.left is not None:
                self.left.put(key, value)
            else:
                self.left = Node(key, value)
        if key > self.key:
            if self.right is not None:
                self.right.put(key, value)
            else:
                self.right = Node(key,value)
        self.update_height()

        if self.left is not None: heightLeft = self.left.height
        else: heightLeft = -1
        if self.right is not None: heightRight = self.right.height

        misbalance = heightLeft- heightLeft

        #left big
        if misbalance >1:
            if self.left.left is not None:
                leftLeft = self.left.left.height
            else:
                leftLeft = -1
            if self.left.right:
                leftRight = self.left.right.height
            else:
                leftRight = -1
            if leftLeft < leftRight:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        
        #right big
        if misbalance <-1:
            if self.right.left is not None:
                rightleft = self.right.left.height
            else:
                rightleft = -1
            if self.right.right:
                rightright = self.right.right.height
            else:
                rightright = -1
            if rightleft > rightright:
                self.right = self.right.rotate_right()
            return self.rotate_left()         
        




    def rotate_left(self):
        """Rotates self down and to the left"""
        newRoot = self.right
        self.right =  newRoot.left
        newRoot.left = self
        self.update_height()
        self.update_height()
        return newRoot
    



    def rotate_right(self):
        """Rotates self down and to the right"""
        newRoot = self.left
        self.left = newRoot.right
        newRoot.right = self
        self.update_height()
        self.update_height()
        return newRoot
    


    def get(self, key):
        """Returns value associated with key. Raises keyerror if key not in mapping."""
        if self.key == key:
            return self.value
        if key < self.key:
            if self.left is not None:
                return self.left.get(key)
            else:
                raise KeyError(f"{key} not in mapping") 
        if key > self.key:
            if self.right is not None:
                return self.right.get(key)
            else:
                raise KeyError(f"{key} not in mapping") 



    def max_node(self):
        """Returns maximum node in subtree"""
        if self.right is not None: return self.right.max_node()
        else:
            return self
    
    def min_node(self):
        """Returns maximum node in subtree"""
        if self.left is not None: return self.left.max_node()
        else:
            return self



    def _swap(self, other):
        """Swaps keys and values in self and other"""
        self.key , other.key = other.key, self.key
        self.value, other.value = other.value, self.value 


    def remove(self, key):
        """Removes key associated with value."""
        if self.key == key:
            if self.left is None:
                self = self.right
                return self
            elif self.right is None:
                self = self.left
                return self
            else:
                maxLeft = self.left.max_node()
                self._swap(maxLeft)
                self.left.remove(key)
                
        elif key < self.key:
            if self.left: return self.left.remove(key)
            else: raise KeyError(f"{key} not in mapping")
        elif key > self.key:
            if self.right: return self.right.remove(key)
            else:raise KeyError(f"{key} not in mapping")

        return self
    


    def preorder(self):
        """Yields key, value pairs in preorder"""
        yield self.key, self.value
        if self.left: yield self.left.preorder()
        if self.right: yield self.right.preorder()

    

    def postorder(self):
        """Yields key, value pairs in postorder"""

        if self.left: yield self.left.postorder()
        if self.right: yield self.right.postorder()      
        yield self.key, self.value

    def inorder(self):
        """Yields keym value pairs in in-order"""
        if self.left is not None: yield self.left.inorder()
        yield self.key, self.value
        if self.right is not None: yield self.right.inorder()        




