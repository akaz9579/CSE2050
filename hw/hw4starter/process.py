class Process:
    def __init__(self, pid, cycle=100,):
        """define variables"""
        self.pid = pid
        self.cycles = cycle
        self.link = None 
        self.prev = None 



    def __eq__(self, other):
        """evaluating if 2 process pid values are equal"""
        if self.pid == other.pid:
            return True
        else:
            return False 
    
    def __repr__(self):
        "sets reper to return pid"
        return f"Process({self.pid},{self.cycles})"
    

   
