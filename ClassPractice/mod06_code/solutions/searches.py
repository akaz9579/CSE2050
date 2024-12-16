def linear_search(item, L):
    """Returns True if item is in L"""
    for i in range(len(L)):
        if item == L[i]: return True
    return False

# O(n) recursive binary search (uses slicing)
def binary_search_slice(item, L):
    """Returns True if item is in L"""
    n = len(L)

    # Base case: empty sublist
    if n == 0: return False

    i_med = n//2

    # Base case: found item
    if item == L[i_med]: return True

    # Recursive cases
    elif item < L[i_med]: return binary_search_slice(item, L[:i_med])
    elif item > L[i_med]: return binary_search_slice(item, L[i_med+1:])

# O(logn) recursive binary search
def binary_search_recr(item, L):
    """Returns True if item is in L"""
    return _binary_search(item, L, i_left=0, i_right=len(L))

def _binary_search(item, L, i_left, i_right):
    """Returns True if item is in L"""
    n = i_right-i_left
    if n == 0: return False

    i_med = (i_left+i_right)//2

    if item == L[i_med]: return True

    elif item < L[i_med]: return _binary_search(item, L, i_left, i_med)
    elif item > L[i_med]: return _binary_search(item, L, i_med+1, i_right)

# O(logn) iterative binary search
def binary_search_iter(item, L):
    """Returns True if item is in L"""
    i_left = 0
    i_right = len(L)

    while i_right-i_left >= 1:
        i_med = (i_left+i_right)//2
        if L[i_med] == item: return True

        elif item < L[i_med]: i_right = i_med
        elif item > L[i_med]: i_left = i_med+1

    return i_right > i_left and item == L[i_left]