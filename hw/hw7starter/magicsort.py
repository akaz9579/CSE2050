import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):

    #tests if the list is sorted.
    #if it not sorted it will pass if case and 
    #will be marked by sorted bool
    sorted = True
    for i in range(len(L)-1): 
        if L[i+1]<L[i]: 
            sorted = False
            break
    if sorted: return MagicCase.SORTED

    #tests if the list is Reverse.
   
    reverse_sorted = True
    for i in range(len(L) - 1):
        if L[i] < L[i + 1]:
            reverse_sorted = False
            break
    if reverse_sorted:
        return MagicCase.REVERSE_SORTED
   
    inversions = 0
    for i in range(len(L)-1): 
        if L[i+1]<L[i]: 
            inversions +=1
    if inversions<=INVERSION_BOUND: return MagicCase.CONSTANT_INVERSIONS

    #if not sorted or reversed or invertion, it will have to be a general case
    return MagicCase.GENERAL


        
def reverse_list(L):
    i = 0
    j = len(L) - 1
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1


def magic_insertionsort(L, left, right, alg_set=None):
    if alg_set is not None:
        alg_set.add('magic_insertionsort')

    for j in range(left+1,right):
        i=j
        while i>left and L[i-1]> L[i]:
            L[i],L[i-1] = L[i-1],L[i]
            i-=1


    

def magic_mergesort(L, left, right, alg_set=None):
    if alg_set is not None:
        alg_set.add('magic_mergesort')

    if right - left <= 1:
        return

    mid = (left + right) // 2

    magic_mergesort(L, left, mid, alg_set)
    magic_mergesort(L, mid, right, alg_set)

    merged = []
    i, j = left, mid

    while i < mid and j < right:
        if L[i] <= L[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(L[j])
            j += 1

    merged.extend(L[i:mid])  
    merged.extend(L[j:right])  

    L[left:right] = merged  



def magic_quicksort(L, left, right, depth=0, alg_set=None):
    if alg_set is not None:
        alg_set.add('magic_quicksort')

    if right - left <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return

    if right - left <= 1:
        return

    max_depth = math.log2(len(L)) * 3
    if depth > max_depth:
        magic_mergesort(L, left, right, alg_set)
        return

    pivot_index = right - 1
    pivot = L[pivot_index]
    i, j = left, right - 2

    while i <= j:
        while i <= j and L[i] < pivot:
            i += 1
        while i <= j and L[j] >= pivot:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[i] > pivot:
        L[i], L[pivot_index] = L[pivot_index], L[i]

    magic_quicksort(L, left, i, depth + 1, alg_set)
    magic_quicksort(L, i + 1, right, depth + 1, alg_set)

def magicsort(L):
    alg_set=set()
    scan = linear_scan(L)
    if scan == MagicCase.SORTED:
        return alg_set
    elif scan == MagicCase.REVERSE_SORTED:
        reverse_list(L)
        alg_set.add("reverse_list")
    elif scan == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L,0,len(L),alg_set)
    else:
        magic_quicksort(L,0,len(L),0,alg_set)

    return alg_set
    




