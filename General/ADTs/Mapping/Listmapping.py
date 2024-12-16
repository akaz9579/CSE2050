class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"


class ListMapping:
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)

    def __setitem__(self, key, value):  # O(n)
        for entry in self.L:
            if entry.key == key:
                entry.value = value  # Assign value
                return
        self.L.append(Entry(key, value))  # Append new entry

    def __getitem__(self, key):  # O(n)
        for entry in self.L:
            if entry.key == key:
                return entry.value
        raise KeyError(f"{key} not found in mapping")

    def delete(self, key):
        for i, entry in enumerate(self.L):
            if entry.key == key:
                self.L.pop(i)  
                return
        raise KeyError(f"{key} not found in mapping")

    def keys(self):
        return [entry.key for entry in self.L]  # Return list of keys

    def values(self):
        return [entry.value for entry in self.L]  # Return list of values

    def items(self):
        return {(entry.key, entry.value) for entry in self.L} 