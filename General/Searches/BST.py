class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.weight = 1
    
    def get(self, key):
        #3 cases, 
        # 1. self.keu == keu, return self, 
        # 2.  self.key> key, go left child,
        #3. self.key < key, go right child
        
        if self.key == key:
            return self.value
        if self.key > key:
            if self.left != None:
                return self.left.get(key)
        if self.key < key:
            if self.right != None:
                return self.right.get(key)
        
        #if none of these cases, then they key isnt in here
        raise KeyError(f"Key{key} is not in BST")

    def put(self,key,value):
        #if key is found, change the value at that key
        if self.key == key:
            self.value = value

        #if key is small, check left children
        elif self.key> key:
            #if the left child exist, keep going down till you find the key
            if self.left:
                self.left.put(key,value)
            #if key was not found, add a new node
            else:
                self.left = BSTNode(key,value)
        #if key is big, check right children
        elif self.key< key:
            #if the right child exist, keep going down till you find the key
            if self.right:
                self.right.put(key,value)     
            #if key was not found, add a new node
            else:
                self.right =BSTNode(key,value)  
        
        self.update_weight
    
    def update_weight(self):
        left_weight = self.left.weight if self.left else 0
        right_weight = self.right.weight if self.right else 0
        self.weight  = left_weight + right_weight

#returns node with its key and value or node with next closet key (less than)
    def floor(self, key):
        #3 cases, self.keu == key, return self, 
        # self.key> key, go left child,
        #self.key < key, go right child       
        if self.key == key:
            return self
        elif self.key > key:
            if self.left:
                return self.left.floor(key)
            else: 
                return None
        elif self.key < key:
            if self.right:
                tempNode = self.right.floor(key)
                if tempNode: 
                    return tempNode
            else:
                return self
            
    def __repr__(self):
         """Returns string repr of just this node"""
         return f"BSTNode({self.key}, {self.value})"

    def __contains__(self, key):
        """Returns True if key in mapping"""
        if key == self.key: return True

        elif key < self.key and self.left is not None:
            return key in self.left
        
        else:
            if self.right is not None:
                return key in self.right
        
        return False
    
    def in_order(self):
        """Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword.
        """
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        yield self.key                                              # return this key
        if self.right is not None: yield from self.right.in_order() # recursively go right

        
                
class BSTMap:
    def __init__(self):
        self.root = None

    def put(self,key,value):
        if self.root:
            self.root.put(key,value)
        else:
            self.root = BSTNode(key, value)

    def get(self,key):
        if self.root:
            self.root.get(key).value
        else:
            raise KeyError(f"key {key} is not in BSTMap")
        
    def floor(self,key):
        if self.root:
            floor_node = self.root.floor(key)
        if floor_node:
            return floor_node.key, floor_node.value
        
        else:
            return None, None
        
    def rotateRight(self, x, y):
        
    

        

