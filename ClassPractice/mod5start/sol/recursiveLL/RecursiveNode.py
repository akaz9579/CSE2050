class Node:
    def __init__(self, data, link=None):
        """Instantiates a new node for a linked list"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length"""
        if self.link is None: return 1 # Base case
        return 1 + len(self.link)     # Recursive case

    def count(self, item):
        """Recursively determines how many instances of item are in list"""
        if self.link is None: # Base case
            return 1 if self.data == item else 0
        
        return self.link.count(item) + (1 if self.data == item else 0)
    
    def add_before(self, old_item, new_item):
        """Adss a node containing new_item just before the first node containing old_item"""
        if self.data == old_item: # base case
            return Node(new_item, link=self) # return the node that should be previous nodes link
        
        else:
            self.link = self.link.add_before(old_item, new_item) # self.link may change, if next item is base case
            return self

def list_reprs(node):
    """Returns list of string reprs of all nodes starting at node"""
    node_reprs = []

    while node.link is not None:
        node_reprs.append(repr(node))
        node = node.link

    node_reprs.append(repr(node))

    return node_reprs
if __name__ == '__main__':
    # Typically we'd use a LinkedList class to track the head,
    # but doing that manually here for the sake of simplicity.

    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')

    # Test len
    assert len(na) == 1
    na.link, nb.link, nc.link, nd.link = nb, nc, nd, ne
    assert len(na) == 5

    # Test count
    assert na.count('c') == 1
    ne.link = Node('c')
    assert na.count('c') == 2



    # test add_before
    print(f"before adding: {list_reprs(na)}")
    na.add_before('c', 'r')
    print(f"after adding: {list_reprs(na)}")