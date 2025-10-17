def bubblesort(L):
    unsorted = True
    while unsorted:
        unsorted = False
        for j in range(len(L)-1):
            for i in range(len(L)-1-j):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    unsorted = True

#O(n^2) in time, 
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
