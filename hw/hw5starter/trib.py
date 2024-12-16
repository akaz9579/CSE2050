def trib(k):
    return _trib(k, solved=dict())

def _trib(k, solved):
    """Helper function for tribonacci"""
    if k in solved: 
        return solved[k]
    
    if k == 0 or k == 1 or k==2:
        solved[k] = 0
        return solved[k]
    if k == 3:
        solved[k] = 1
        return solved[k] 

    solved[k] = _trib(k-1, solved) + _trib(k-2, solved) + _trib(k-3, solved)

    
    return solved[k]

print(trib(100))