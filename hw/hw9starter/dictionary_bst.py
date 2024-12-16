class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.weight = 1



class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    #def __iter__(self,s);
        
    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        self.root = self.recursive(self.root, word, meaning)
    
    
    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        node = self.search_recursive(self.root, word)
        return node.meaning if node else None 

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        result = []
        self.in_order(self.root, result)
        return result

    # Feel free to implement other helper and private methods


    def recursive(self, node, word, meaning):
        if node is None:
            return Node(word, meaning)
        if word < node.word:
            node.left = self.recursive(node.left, word, meaning)
        elif word > node.word:
            node.right = self.recursive(node.right, word, meaning)
        else:
            node.meaning = meaning 
            return node

        node.weight = 1 + max(self.get_weight(node.left), self.get_weight(node.right))
        return self.balance(node, word)
    
    def search_recursive(self, node, word):
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self.search_recursive(node.left, word)
        else:
            return self.search_recursive(node.right, word)

    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append((node.word, node.meaning))
            self.in_order(node.right, result)

    def get_weight(self, node):
        return node.weight if node else 0

    def get_balance(self, node):
        return self.get_weight(node.left) - self.get_weight(node.right) if node else 0

    def balance(self, node, word):
        balance_factor = self.get_balance(node)

        # left
        if balance_factor > 1:
            if word < node.left.word:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance_factor < -1: #rigth
            if word > node.right.word:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.weight = 1 + max(self.get_weight(z.left), self.get_weight(z.right))
        y.weight = 1 + max(self.get_weight(y.left), self.get_weight(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.weight = 1 + max(self.get_weight(z.left), self.get_weight(z.right))
        y.weight = 1 + max(self.get_weight(y.left), self.get_weight(y.right))
        return y

