class Entry:
    def __init__(self, key, value):
        """Creates a new entry object"""
        self.key = key
        self.value = value

    def __repr__(self):
        """Returns string representation of obj"""
        return f"Entry({self.key}, {self.value})"
    
class Mapping:
    def __init__(self):
        """Creates a new mapping"""
        self._L = [] # list of Entry objects

    def __setitem__(self, key, value):
        """Adds key:value pair or updates value associated w/ key"""
        self._L.append(Entry(key, value))

    def __getitem__(self, key):
        """Returns value associated w/ key; raises KeyError if key not in mapping"""
        n = len(self._L)
        # iterate through self._L backwards, looking for a matching key
        for i in range(n):
            if self._L[n-1-i].key == key:
                return self._L[n-1-i].value
            
        raise KeyError("Key {key} not in mapping")


if __name__ == '__main__':
    m1 = Mapping()                                  # __init__
    m1['jake'] = ['cse2050', 'cse3666']             # __setitem__
    m1['lina'] = ['cse2050', 'cse3500']             # __setitem__
    assert m1['jake'] == ['cse2050', 'cse3666']     # __getitem__

    # Check that __getitem__ looks at newer entry
    m1['jake'] = ['cse3100']
    assert m1['jake'] == ['cse3100']
    
    # Check that we get a Key Error when getting a non-existing key
    try:
        m1['tim']
        raise AssertionError
    except KeyError:
        pass

    print("all good")