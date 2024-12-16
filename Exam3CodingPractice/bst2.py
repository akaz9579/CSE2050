
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
        if self.right: 
            heightRight = self.right.height
        else:
            heightRight = -1
        if self.left:
            heightleft = self.left.height
        else:
            heightleft = -1
        self.height = max(heightRight, heightleft) +1




    def put(self, key, value):
        """Adds key:value pair, or updates value if key already in mapping"""
        if key == self.key:
            return self.value
        elif key < self.key:
            if self.left: return self.left.put(key, value)
            else: self.left = Node(key, value)
        else:
            if self.right: return self.right.put(key,value)
            else: self.right = Node(key, value)

        self.update_height()


        if self.right: 
            heightRight = self.right.height
        else:
            heightRight = -1
        if self.left:
            heightleft = self.left.height
        else:
            heightleft = -1

        misbalance =  heightleft - heightRight

        if misbalance > 1:
            if self.left.left: 
                leftLeft = self.left.left.height
            else:
                leftLeft = -1
            if self.left.right: 
                leftright = self.left.right.height
            else:
                leftright = -1
            
            if leftLeft > leftright: self.left = self.left.rotate_left()
            return self.rotate_right()
        
        if misbalance < -1:
            if self.right.left: 
                rightLeft = self.right.left.height
            else:
                leftLeft = -1
            if self.right.right: 
                rightright = self.right.right.height
            else:
                rightright = -1
            
            if rightright > rightLeft: self.right = self.right.rotate_right()
            return self.rotate_left()




    def rotate_left(self):
        """Rotates self down and to the left"""
        newRoot = self.right
        self.left = self.right.left
        newRoot.left = self
        self.update_height()
        self.update_height()
        return newRoot
 
    def rotate_right(self):
        """Rotates self down and to the right"""
        newRoot = self.left
        self.left = self.left.right
        newRoot.right = self
        self.update_height()
        self.update_height()
        return newRoot
    


    def get(self, key):
        """Returns value associated with key. Raises keyerror if key not in mapping."""
        if key == self.key:
            return self.value
        elif key < self.key:
            if self.left: return self.left.get(key)
            else: raise KeyError(f"{key} not in mapping")
        else:
            if self.right: return self.right.get(key)
            else: raise KeyError(f"{key} not in mapping")
        

            



    def max_node(self):
        """Returns maximum node in subtree"""
        if self.right: return self.right.max_node()
        else: return self

 
    def min_node(self):
        """Returns maximum node in subtree"""
        if self.left: return self.left.min_node()
        else: return self



    def _swap(self, other):
        """Swaps keys and values in self and other"""
        self.key, other.key = other.key, self.key
        self.value, other.value = other.key, self.key


    def remove(self, key):
        """Removes key associated with value."""
        if key == self.key:
            if self.left is None:
                self = self.right
                return self
            if self.right is None:
                self = self.right
                return self
            else:
                maxLeft = self.left.max_node()
                self._swap(maxLeft)
                self.left.remove(key)

        elif key < self.key:
            if self.left: return self.left.remove(key)
            else: raise KeyError(f"{key} not in mapping")
        else:
            if self.right: return self.right.remove(key)
            else: raise KeyError(f"{key} not in mapping")


    def preorder(self):
        """Yields key, value pairs in preorder"""
        yield self.key, self.value
        if self.right: yield self.right.preorder()
        if self.left: yield self.left.preorder()

    

    def postorder(self):
        """Yields key, value pairs in postorder"""
        if self.right: yield self.right.postorder()
        if self.left: yield self.left.postorder()
        yield self.key, self.value


    def inorder(self):
        """Yields keym value pairs in in-order"""
        if self.right: yield self.right.inorder()
        yield self.key, self.value
        if self.left: yield self.left.inorder()




