from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn."""
    def __init__(self, processes=None):
        """Initialization of variables."""
        self._head = None
        self._len = 0
        self._d_processes = {}  

        if processes is not None:
            for process in processes:
                self.add_process(process)

    def __len__(self):
        """Returns the length of the queue."""
        return self._len
    
    def __repr__(self):
        """String representation of the CircularQueue."""
        if not self._head:
            return "CircularQueue()"
        
        processes = []
        current = self._head
        while True:
            processes.append(f"Process({current.pid},{current.cycles})")
            current = current.link
            if current == self._head:
                break

        return f"CircularQueue({', '.join(processes)})"

    def add_process(self, process):
        """Adds a process to the queue."""
        self._d_processes[process.pid] = process 
        self._len += 1
        if self._head is None:
            self._head = process
            process.link = process
            process.prev = process
        else:
            self._head.prev.link = process
            process.prev = self._head.prev
            process.link = self._head
            self._head.prev = process

    def remove_process(self, process):
        """Removes a process from the queue."""
        if self._head is None:
          raise RuntimeError("Can't remove from an empty queue")

        old = process

        del self._d_processes[process.pid]

        if self._head == self._head.prev: 
           self._head = None
        else:
            prev_process = process.prev
            next_process = process.link
            prev_process.link = next_process
            next_process.prev = prev_process

            if process == self._head:
                self._head = next_process

        self._len -= 1
        return old


    def kill(self, pid):
        """Removes and returns the process with the given pid."""
        if pid not in self._d_processes:
            raise KeyError(f"Process with '{pid}' not found")
        process = self._d_processes[pid]
        self.remove_process(process)
        return process



    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time."""
        n_remaining = n_cycles
        return_strings = []   

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles - n_remaining + 1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)



