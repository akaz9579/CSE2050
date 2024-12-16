def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-2))

assert is_sorted([-3,-3,-3])
assert is_sorted([-3,-2,-1])
assert not is_sorted([-3,2,1])


def bubblesort(L):
    n = len(L)

    for j in range(n-1):
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

def bubbleAdapr(L):
    n = len(L)
    
    ISsorted = False 
    j = 0
    while not ISsorted:
        ISsorted =True        
        
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                ISsorted = False
                L[i], L[i+1] = L[i+1], L[i]

        j+1




L= [n-1 for i in range(n)]
bubblesort(L)

