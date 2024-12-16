def quicksort(L):
    _quicksort(L, left =0, right= len(L))

def _quicksort(L, left, right):
    if right-left <2:
        return
    
    pivot = partition(L, left,right)
    _quicksort(L, left,pivot)
    _quicksort(L, right,pivot)

def partition(L, left, right):
    i = left
    pivot = right - 1
    j = pivot-1

    while i<j:
        while L[i] < L[pivot]:
            i+=1
        while i< j and L[j] >= L[pivot]:
            j-=i
        if i<j: 
            L[i], L[j]= L[j], L[i]

    L[i], L[pivot]= = L[pivot], L[i]
    pivot = i
    
    return pivot
