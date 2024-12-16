# Mod 08 - Mappings and Hashtables

Implement the empty methods below.

```python
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
        i_bkt = hash(key) % self.n_buckets
        for e in self._L[i_bkt]:
            if key == e.key:
                e.value = value
                return
        
        self._L[i_bkt].append(Entry(key, value))
        self._len += 1

        # Rehash if loadfactor too high
        alpha = len(self) / self.n_buckets
        if alpha > self.max_alpha:
            self.rehash(n_new = 2*self.n_buckets)


    def __getitem__(self, key, value):
        """Returns value associated with key. Raises keyerror if key not in mapping."""
        i_bkt = hash(key) % self.n_buckets
        for e in self._L[i_bkt]:
            if key == e.key: return e.value
        raise KeyError(f"Key {key} not found.")  
    
    def remove(self, key):
        """Removes key associated with value. Raises keyerror if key not in mapping."""
        i_bkt = hash(key) % self.n_buckets
        for e in self._L[i_bkt]:
            if key == e.key:
                self._L.remove(e)
                self._len -= 1
                
                # rehash if loadfactor too low
                alpha = len(self) / self.n_buckets
                if alpha < self.min_alpha and alpha//2 >= self.min_buckets:
                    self.rehash(n_new = self.n_buckets//2)
                return

        raise KeyError(f"Key {key} not found.")


    def rehash(self, n_new):
        """Rehashes to n_new buckets"""
        self.n_buckets *= n_new
        new_L = [[] for i in range(self.n_buckets)]

        for bucket in self._L:
            for entry in bucket:
                i = hash(entry.key) % self.n_buckets
                new_L[i].append(entry)

        self._L = new_L
```