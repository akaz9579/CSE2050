import random

def merge_sort(L):
    """Sorts w/ merge sort"""
    # Base case - a list of 1 or 0 items is already sorted
    if len(L) < 2: return L

    # Recursive case - sort left and right halves, then merge them
    L_left = merge_sort(L[:len(L)//2])
    L_right = merge_sort(L[len(L)//2:])
    merge(L, L_left, L_right)

    # Return statement necessary for recursive cases
    return L

def merge(L, L_left, L_right):
    """Merges sorted lists L_left and L_right into L"""
    i, j = 0, 0

    while i < len(L_left) and j < len(L_right):
        # For stability, write from L_left if items are equal
        if L_left[i] <= L_right[j]:
            L[i+j] = L_left[i]
            i+=1

        else:
            L[i+j] = L_right[j]
            j+=1

    # Append the rest of L_left or L_right, whichever is not finished yet
    L[i+j:] = L_left[i:] + L_right[j:]

if __name__ == '__main__':
    ### Test merge ###
    L1 = [1, 3, 5, 7, 9]
    L2 = [2, 4, 6, 8, 10]
    L = [None for i in range(len(L1)+len(L2))]

    merge(L, L1, L2)
    assert L == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for repeats in range(100):                          # repeat test 100 times
        # Setup random lists
        n = 1000
        L1 = [random.randint(0, n) for i in range(n)]   # create random list 1
        L2 = [random.randint(0, n) for i in range(n)]   # create random list 2
        L = L1 + L2                                     # List large enough to contain L1 and L2 (don't care about contents)
        
        # Sort L1 and L2, create sorted solution
        L1.sort()
        L2.sort()
        L_sol = L1 + L2
        L_sol.sort()

        # Test
        merge(L, L1, L2)
        assert L == L_sol

    ### Test mergesort ###
    n = 10000
    L = [random.randint(0, n) for i in range(n)]
    L2 = L[:]
    L2.sort()

    merge_sort(L)
    assert L == L2