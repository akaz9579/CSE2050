
def idx_left(L, idx, right):
    """Return index of left child, or None if not less than right."""
    i_l = 2 * idx + 1
    return i_l if i_l < right else None

def idx_right(L, idx, right):
    """Return index of right child, or None if not less than right."""
    i_r = 2 * idx + 2
    return i_r if i_r < right else None

def idx_max_child(L, idx, right):
    """Return index of max child, or None if not less than right."""
    i_l = idx_left(L, idx, right)
    i_r = idx_right(L, idx, right)
    if i_l is None:
        return None
    elif i_r is None:
        return i_l
    else:
        return i_l if L[i_l] > L[i_r] else i_r

def swap(L, i, j):
    """Swaps items at indices i and j."""
    L[i], L[j] = L[j], L[i]

def downheap(L, idx, right):
    """Downheaps the item at index idx to maintain max-heap property."""
    while True:
        max_child_idx = idx_max_child(L, idx, right)
        if max_child_idx is None or L[idx] >= L[max_child_idx]:
            break
        swap(L, idx, max_child_idx)
        idx = max_child_idx

def heapsort(L):
    """Sorts the list L in place using heapsort algorithm."""
    n = len(L)

    for i in reversed(range(n // 2)):
        downheap(L, i, n)

    for i in range(n - 1, 0, -1):
        swap(L, 0, i)  
        downheap(L, 0, i)  
