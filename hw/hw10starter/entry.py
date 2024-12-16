class Entry:
    def __init__(self, item, priority):
        """Creates new object """
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """equal if their priorities are equal"""
        return self.priority == other.priority


    def __lt__(self, other):
        """compared based on priority"""
        return self.priority < other.priority

    def __le__(self, other):
        """ compared based on priority"""
        return self.priority <= other.priority


    def __repr__(self):
        """string representation of Entry"""
        return f"Entry(item={self.item}, priority={self.priority})"
