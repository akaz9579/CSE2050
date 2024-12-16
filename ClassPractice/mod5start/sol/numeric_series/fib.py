def fib(k):
    """Returns the kth fibonacci number"""
    if k == 0: return 0
    elif k == 1: return 1
    return fib(k-1) + fib(k-2)

def fib(k, solved={0:0, 1:1}):
    if k in solved: return solved[k]

    solved[k] = _fib(k-1, solved) + _fib(k-2, solved)

    return solved[k]

def fib_memo(k):
    """Recursively calculates the nth fibonacci using memoization"""
    solved = {0:0, 1:1} # Dictionary of solved subproblems
    return _fib(k, solved) # Pass to a helper function

def _fib(k, solved):
    """Helper function for fib_memo"""
    # Base case - I've solved this subproblem
    if k in solved: return solved[k]

    solved[k] = _fib(k-1, solved) + _fib(k-2, solved)

    return solved[k]

fib_memo(35)

if __name__ == '__main__':
    sols = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55}

    for key in sols:
        assert fib(key) == sols[key]
        assert fib_memo(key) == sols[key]
