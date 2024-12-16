def linear_search(item, L):
    """Returns True if item is in L"""
    for i in range(len(L)):
        if item == L[i]: return True
    return False

def bs_bad(item, L):
    """Returns True if item is in L"""
    #bad because slicing takes o(n) time, too long 
    n = len(L)

    if n == 0:
        return False
    
    mid = n//2

    if L[mid] == item:
        return True
    elif item < L[mid]:
        return bs(item, L[:mid]) 
    elif item > L[mid]:
        return bs(item, L[mid+1:])
    
    return False


def bs_good(item, L, start, end):
    """Returns True if item is in L"""
    # not slicing, o(logn) time now, o(n) meomory
    n = end - start

    if n == 0:
        return False
    
    mid = (start+end) //2

    if L[mid] == item:
        return True
    elif item < L[mid]:
        return bs_good(item, L, start, mid) 
    elif item > L[mid]:
        return bs_good(item, L, mid+1, end)
    
    return False

def bs_iter(item, L):
    """Returns True if item is in L"""
    # not slicing, o(logn) time now, o(1) memory
    start = 0
    end = len(L)

    while start<end:
        mid = (start + end)//2
        if L[mid] == item:
            return True
        elif item < L[mid]:
            end = mid
        elif item > L[mid]:
            start = mid+1

    return False