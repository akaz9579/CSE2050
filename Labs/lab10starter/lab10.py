class Entry:
    def __init__(self, item, priority):
        """Instantiates a new entry object"""
        self.priority = priority
        self.item = item

    def __eq__(self, other):
        """Entries are equal if their priorities are equal"""
        return self.priority == other.priority and self.item == other.item

    def __lt__(self, other):
        """Entries are compared based on priority"""
        return self.priority < other.priority


class PQ_OL:
    def __init__(self):
        self._entries = []

    def insert(self, priority, item):
        self._entries.append(Entry(item, priority))
        self._entries.sort(reverse=True)  

    def find_min(self):
        return self._entries[-1]  

    def remove_min(self):
        return self._entries.pop()  

    def __len__(self):
        return len(self._entries)


class PQ_UL:
    def __init__(self):
        self._entries = []

    def insert(self, priority, item):
        self._entries.append(Entry(item, priority))

    def find_min(self):
        return min(self._entries)  

    def remove_min(self):
        entry = min(self._entries)
        self._entries.remove(entry)
        return entry  

    def __len__(self):
        return len(self._entries)