import random

def merge_sort(L):
    """Sorts w/ merge sort"""

def merge(L, L_left, L_right):
    """Merges sorted lists L_left and L_right into L"""

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

    # ### Test mergesort ###
    # n = 10000
    # L = [random.randint(0, n) for i in range(n)]
    # L2 = L[:]
    # L2.sort()

    # merge_sort(L)
    # assert L == L2