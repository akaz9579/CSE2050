class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"


class HashMap:
    def __init__(self):
        self._len = 0
        self.nBuckets = 100
        self.L = [[] for i in range(self.nBuckets)]

    def __len__(self):
        return self._len

    def __setitem__(self, key, value):  # O(1)
        bucket = self.hash(key) 

        for entry in self.L[bucket]:
            if entry.key == key:
                entry.value = value
                return
        
        self.L[bucket].append(Entry(key,value))
        self._len +=1

        if len(self) > self.nBuckets:
            self.rehash()


    def __getitem__(self, key):  # O(n)
        bucket = self.hash(key) 
        for entry in self.L[bucket]:
            if entry.key == key:
                return entry.value
        raise KeyError(f"{key} Not in mapping")
    

    def __contains__(self, key):
        """Returns true if key in map"""
        i_bucket = hash(key) % self.nBuckets
        for entry in self.L[i_bucket]:
            if entry.key == key: return True                

    def hash(self,key):
        return hash(key) % self.nBuckets
    
    def rehash(self):
        self.nBuckets *=2
        newList = [[]for i in range(self.nBuckets)]
        for bucket in self.L:
            for entry in bucket:
                newBucket = self.hash(entry.key)
                newList[newBucket].append(entry)
        
        self.L = newList[:]







    def delete(self, key):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass 

if __name__ == "__main__":
    m = HashMap()
    n = 100000
    for i in range(n):
        m[i] = str(i)
    
    for i in range(n):
        assert m[i] == str(i)

    print("all good")
    
