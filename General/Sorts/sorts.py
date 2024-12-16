def bubblesort(L):
    unsorted = True
    while unsorted:
        unsorted = False
        for j in range(len(L)-1):
            for i in range(len(L)-1-j):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    unsorted = True

#O(n^2 in time, 
#O(1) in memory

def selection(L):
    for j in range(len(L)):
        minIndex = j
        for i in range(j+1,len(L)):
            if L[i] < L[minIndex]:
                minIndex = i
        L[j],L[minIndex] = L[minIndex], L[j]

#O(n^2) for time,
#lil better than bubble because doesnt do as many reads and rights,
# but can't leave early, non adaptable.


def insertionsort(L):
   for i in range (1,len(L)):
       j=i
       while L[j-1]>L[j] and j>0:
           L[j-1],L[j]= L[j],L[j-1]
           j-=1




def merge_sort(L):
    """Sorts w/ merge sort"""
    # Base case - a list of 1 or 0 items is already sorted
    if len(L) < 2: 
        return L

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
    

def quick_bad(L):
    if len(L) <= 1:
        return L  # Base case: list with 0 or 1 element is already sorted
    
    pivot = L[-1]  # Last element as pivot
    i = 0
    j = len(L) - 2  # Exclude pivot from the loop
    
    # Partition step
    while i <= j:
        # Find the first element greater than or equal to the pivot
        if L[i] > pivot:
            # Find the first element less than the pivot from the right side
            if L[j] < pivot:
                # Swap L[i] and L[j]
                L[i], L[j] = L[j], L[i]
            else:
                j -= 1
        else:
            i += 1

    # Place pivot in the correct position
    L[i], L[-1] = L[-1], L[i]

    # Recursively apply quicksort to the sublists
    left = quick_bad(L[:i])      # Elements before pivot
    right = quick_bad(L[i+1:])   # Elements after pivot

    return left + [L[i]] + right  # Combine sorted sublists and pivot


def quick_good(L, left = 0, right = None):
    if right == None:
        right = len(L)
    if right - left <=1:
        return None
    pivot = right -1

    i=left
    j = right -2

    while i<j:
        while L[i]< L[pivot]:
            i+=1
        while L[j]>= L[pivot] and i<j:
            j-=1    
        if i<j:
            L[i], L[j]= L[j], L[i]
    
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[j],L[i]
        pivot = i

    quick_good(L,left, pivot)
    quick_good(L,pivot+1, right)



    