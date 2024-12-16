class BSTNode:
    def __init__(self, key, value, left = None,  right= None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def put(self, key, value):
        #key we are loooking for:
        if key == self.key: self.value = value 
        elif key < self.key: #go left
            if self.left is None:
                self.left = BSTNode(key,value)
            else:
                self.left.put(key,value)
        else:  #go right 
            if self.right is None:
                self.right = BSTNode(key,value)
            else:
                self.right.put(key,value)

    def get(self,key):
        #
        if key == self.key: return self.value 
        elif key < self.key:
            if self.left is not None: return self.left.get(key)
        else:
            if self.right is not None: return self.right.get(key)
        
        raise KeyError("key not found")

    def __contains__(self , key):
        if key == self.key: return True
        elif key < self.key:
            if self.left is not None: return key in self.left
        else:
            if self.right is not None: return key in self.right
        
        return False    


    def __repr__(self):
        return f"BSTnode({self.key}, {self.value})"
    
if __name__ == '__main__':
    root =  BSTNode("jake",0)
    assert root.get("rachel") == 1
    assert "jake" in root
    assert "rachel" in root

    root.put('rachel',1)
    assert root.get("jake") ==0
    assert root.get("rachel") == 1
        