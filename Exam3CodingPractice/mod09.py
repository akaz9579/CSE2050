
class Node:
    def __init__(self, key, value):
        """Creates a new node with key and value"""
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def update_height(self):
        """Updates height of this node"""
        if self.left: heightLeft = self.left.height
        else: heightLeft = -1

        if self.right: heightright = self.right.height
        else: heightright = -1

        self.height = max(heightLeft, heightright) +1


    def put(self, key, value):
        """Adds key:value pair, or updates value if key already in mapping"""
        if self.key == key: self.value = value

        if self.key > key: 
            if self.left:
                self.left.put(key, value)
            else:
                self.left = Node(key,value)

        if self.key < key: 
            if self.right:
                self.right.put(key, value)
            else:
                self.right = Node(key,value)

        self.update_height()

        if self.left is not None:
            heightLeft = self.left.height
        else:
            heightLeft = -1
        
        if self.right is not None:
            heightRight = self.right.height
        else:
            heightRight = -1

        
        misbalanced = heightLeft - heightRight > 1

        #left big
        if misbalanced > 1:
            if self.left.left is not None:
                leftLeft = self.left.left.height
            else:
                leftLeft = -1
            if self.left.right is not None:
                leftRight = self.left.right.height
            else:
                leftRight = -1

            if leftRight > leftLeft:  # Left-Right case
                self.left = self.left.rotate_left()

            # Left-Left case (or after fixing Left-Right)
            return self.rotate_right()
            

        #right big
        if misbalanced < -1:
            if self.right.left is not None:
                rightLeft = self.right.left.height
            else:
                rightLeft = -1
            if self.right.right is not None:
                rightRight = self.right.right.height
            else:
                rightRight = -1

            if rightRight < rightLeft:  
                self.right = self.right.rotate_right()

            return self.rotate_left()
          
         
    def rotate_left(self):
        """Rotates self down and to the left"""
        root = self.right
        self.right = root.left
        root.left = self
        self.update_height()
        root.update_height()
        return root

    def rotate_right(self):
        """Rotates self down and to the right"""
        root = self.left
        self.left = root.right
        root.right = self
        self.update_height()
        root.update_height()
        return root


    def get(self, key):
        """Returns value associated with key. Raises keyerror if key not in mapping."""   
        if self.key == key:
            return self.value
        if key< self.key:
            if self.left:
                return self.left.get(key)
            else: raise KeyError(f"{key} not in mapping")
        if key >self.key:
            if self.right:
                return self.right.get(key)  
            else: raise KeyError(f"{key} not in mapping")

    def max_node(self):
        """Returns maximum node in subtree"""
        if self.right is not None: 
            return self.right.max_node()
        else:
            return self


    def _swap(self, other):
        """Swaps keys and values in self and other"""
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value


    def remove(self, key):
        """Removes key associated with value."""
        if self.key == key:
            #no left kid, means taking out root would only be enitre right
            if self.left is None: 
                return self.right
            #no right kid, means taking out root would only be enitre left
            elif self.right is None: 
                return self.left
            else:
                max_left = self.left.max_node()
                self._swap(max_left)
                self.left = self.left.remove(key)
        elif key < self.key:
            self.left = self.left.remove(key)
        else:
            self.right.remove(key)
        
        return self
    

    def preorder(self):
        """Yields key, value pairs in preorder"""
        yield self.key, self. value 
        if self.left is not None: yield self.left.preorder()
        if self.right is not None: yield self.right.preorder()
        

    def postorder(self):
        """Yields key, value pairs in postorder"""

        if self.left is not None: yield self.left.postorder()
        if self.right is not None: yield self.right.postorder()
        yield self.key, self. value 


    def inorder(self):
        """Yields keym value pairs in in-order"""
        if self.left is not None: yield self.left.inorder()
        yield self.key, self. value 
        if self.right is not None: yield self.right.inorder()



