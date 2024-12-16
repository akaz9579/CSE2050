
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self):
        """Initializes a new, empty hashmap"""
        self.n_buckets = 8
        self.min_buckets = 8
        self.min_alpha = 0.5
        self.max_alpha = 1
        self._L = [[] for _ in range(self.n_buckets)]
        self._len = 0

    def __len__(self):
        """Returns number of key:value pairs in hash map"""
        return self._len

    def __setitem__(self, key, value):
        """Adds key:value pair, or updates value if key already in mapping"""
        buckets = hash(key)% self.n_buckets
        for entry in self._L[buckets]:
            if entry.key == key:
                entry.value = value 
                return
        self._L[buckets].append(Entry(key,value))
        self._len +=1

        alpha = len(self._L) / self.n_buckets
        if alpha > self.max_alpha:
            self.rehash(2*self.n_buckets)

        
        

    def __getitem__(self, key, value):
        """Returns value associated with key. Raises keyerror if key not in mapping."""
        buckets = hash(key)% self.n_buckets
        for entry in self._L[buckets]:
            if entry.key == key:
                return entry.value
        raise KeyError(f"{key} not in mapping")
     



    def remove(self, key):
        """Removes key associated with value. Raises keyerror if key not in mapping."""
        buckets = hash(key)% self.n_buckets
        for entry in self._L[buckets]:
            if entry.key == key:
                self._L[buckets].remove(entry)
                self._len -=1

                alpha = len(self) / self.n_buckets
                if alpha < self.min_alpha and alpha//2 >= self.min_buckets:
                    self.rehash(self.n_buckets//2)
                return
    
        raise KeyError(f"{key} not in mapping")





    def rehash(self, n_new):
        """Rehashes to have n_new buckets"""
        self.n_buckets = n_new
        newList = [[]for i in range(self.n_buckets)]

        for bucket in self._L:
            for entry in bucket:
                i = hash(entry.key)%self.n_buckets
                newList[i].append(entry)
        
        self._L = newList











