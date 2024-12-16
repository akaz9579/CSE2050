# Mod 09 - Binary Search trees

Implement the empty methods below to complete the BST implementation of the mapping ADT with O(logn) put and get operations.

```python
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
        hl = self.left.height if self.left else -1
        hr = self.right.height if self.right else -1
        self.height = 1 + max(hl, hr)

    def put(self, key, value):
        """Adds key:value pair, or updates value if key already in mapping"""
        if key == self.key:
            self.value = value
            return self

        elif key < self.key:
            self.left = self.left.put(key, value) if self.left else Node(key, value)

        else:
            self.right = self.right.put(key, value) if self.right else Node(key, value)

        self.update_height()

        misbalance = hl - hr
        # left is too tall
        if misbalance > 1:
            # preliminary rotation needed if extra nodes on inner leg.
            h_outer = self.left.left.height if self.left.left else -1
            h_inner = self.right.right.height if self.left.right else -1
            if h_inner > h_outer: self.left = self.left.rotate_left()
        
            # tree is balanced after this
            return self.rotate_right()

        # right is too tall
        elif misbalance < -1:
            # preliminary rotation needed if extra nodes on inner leg
            h_outer = self.right.right.height if self.right.right else -1
            h_inner = self.right.left.height if self.right.left else -1
            if h_inner > h_outer: self.right = self.right.rotate_right()
            
            # tree is balanced after this
            return self.rotate_left()

        return self

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
        if self.key == key: return self.value

        elif key < self.key:
            if self.left: return self.left.get(key)
        
        else:
            if self.right: return self.right.get(key)

        raise KeyError(f"Key {key} not found.")

    def max_node(self):
        """Returns maximum node in subtree"""
        return self.right.max_node() if self.right else self

    def _swap(self, other):
        """Swaps keys and values in self and other"""
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value

    def remove(self, key):
        """Removes key associated with value."""
        if self.key == key:
            if self.left is None: return self.right
            elif self.right is None: return self.left
            else:
                max_left = self.left.max_node()
                self._swap(max_left)
                self.left = self.left.remove(key)
        
        elif key < self.key: 
            self.left = self.left.remove(key)

        else: self.right = self.right.remove(key)

        return self

    def preorder(self):
        """Yields key, value pairs in preorder"""
        yield self.key, self.value
        if self.left is not None: yield from self.left.preorder()
        if self.right is not None: yield from self.right.preorder()

    def postorder(self):
        """Yields key, value pairs in postorder"""
        if self.left is not None: yield from self.left.postorder()
        if self.right is not None: yield from self.right.postorder()
        yield self.key, self.value
    
    def inorder(self):
        """Yields keym value pairs in in-order"""
        if self.left is not None: yield from self.left.inorder()
        yield self.key, self.value
        if self.right is not None: yield from self.right.inorder()
```