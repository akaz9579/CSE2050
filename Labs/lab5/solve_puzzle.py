def _solve_puzzle(L, idx,visited):
    """Checks for the base case if the current index is the final one, then predicts next possible moves, then checks if we have already determined if the next moves work given back to the visited set, and returns true if we can get to the end and false"""
   
    if idx  == len(L)-1:
        return True
    
    idx_cw = (idx+L[idx]) % len(L) 
    idx_ccw = (idx-L[idx]) % len(L)

    #next_move = set()


    if idx in visited:
        return False
    else:
        visited.add(idx)
    

    
    if _solve_puzzle(L,idx_cw,visited):
        return True
    elif _solve_puzzle(L,idx_ccw,visited):
        return True
    else:
        return False


        
def solve_puzzle(L):
    """ takes user's input of L and then uses that value to calls back to the private method """
    return _solve_puzzle(L, idx=0, visited=set())

