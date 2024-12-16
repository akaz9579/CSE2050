# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0): 
        """initilize"""
        self.pos = (round(pos[0], precision), round(pos[1], precision))
        self.max = max
        self.min = min     

    def add_report(self, temp):
        """Update max and min temperatures based on a new report """
        if self.max is None or temp > self.max:
            self.max = temp
        if self.min is None or temp < self.min:
            self.min = temp

    def __eq__(self, other):
        """compared based on position"""
        return isinstance(other, LocalRecord) and self.pos == other.pos

    def __hash__(self): 
         """has based on position"""
         return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self): 
        """initalize"""
        self.size = 16  
        self.records = [[] for _ in range(self.size)]
        self.count = 0

    def __len__(self): 
        """number of postions"""
        return self.count
    
    def add_report(self, pos, temp):
        """Add or update a temperature report for the given position"""
        index = self._get_index(pos)
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        # Check for existing recir
        for record in self.records[index]:
            if record.pos == rounded_pos:
                record.add_report(temp)
                return
        
        # Create a new Record if not found
        new_record = LocalRecord(rounded_pos)
        new_record.add_report(temp)
        self.records[index].append(new_record)
        self.count += 1  
        
        if self.count / self.size > 0.7:
            self._rehash(self.size * 2)


    def __getitem__(self, pos): 
        """(min, max) tuple for a given position"""
        index = self._get_index(pos)
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))

        for record in self.records[index]:
            if record.pos == rounded_pos:
                return (record.min, record.max)

        raise KeyError(f"No records for position {rounded_pos}.")
    
    def __contains__(self, pos): 
        index = self._get_index(pos)
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))

        for record in self.records[index]:
            if record.pos == rounded_pos:
                return True
        return False

    def _rehash(self, m_new): 
        old_records = self.records
        self.size = m_new
        self.records = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_records:
            for record in bucket:
                self.add_report(record.pos, record.max)
                self.add_report(record.pos, record.min)




#used for helper
    def _get_index(self, pos):
        """
        find index for a position in the hash table.
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        return hash(rounded_pos) % self.size

