def fewestcoins_recr(amt, coins):
    """"""
    pass


def reverse_string(string):
    if len(string) == 1:
        return string[0]
    
    return string[-1] + reverse_string(string[0:len(string)-1])


class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link
 
    #######################################################
    # All methods below should be implemented recursively #
    #######################################################
 
    def __len__(self):
        """"""
 
    def __repr__(self):
        """"""
 
    def get_tail(self):
        """"""
 
    def add_last(self, item):
        """"""
 
    # sum_all should return the sum of all items in the linked list
    def sum_all(self):
        """"""
 
    def contains(self, item):
        """"""
 
    # remove_all should remove all nodes that contain a given item
    def remove_all(self, item):
        """"""
 
    def reverse(self):
        """"""
 
#########################################################
# No changes below this point - all your work should be #
# in LLNode.                                            #
#########################################################
class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering
 
    def add_first(self, item):
        """Adds to beginning of Linked List"""
        self._head = LLNode(item, self._head)
 
    def remove_first(self):
        """Removes and returns first item"""
        # Edge case
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty list.')
        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item
 
    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)
 
    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0
 
    def __contains__(self, item):
        """Returns True if item is in Linked List. Returns False otherwise."""
        if self._head is None:
            return False
        return self._head.contains(item)
 
    def add_last(self, item):
        """Adds item to end of Linked List"""
        if self._head is None:
            return self.add_first(item)
        self._head.add_last(item)
 
    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0
 
    def remove_all(self, item):
        """Removes all occurrences of item from Linked List"""
        if self._head is not None:
            self._head = self._head.remove_all(item)
 
    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        if self._head is not None:
            self._head = self._head.reverse()
 
    def get_tail(self):
        """Returns the item stored in tail"""
        return self._head.get_tail() if self._head else None



#Implement a binary search using recursion. 
# It should have a running time of O(logn) and 
# return the index of the first occurence of an item in L, 
# or None if the item is not in L.

def bs_index(item, L ):
    """"""
    return bs_indexHelp(item, L)

def bs_indexHelp(item, L, left=0, right =None):
    if right == None:
        right = len(L)-1
    
    if left>right:
        return None
    mid = (left+right)//2

    if L[mid] == item:
        return mid
    if L[mid]>item:
        return bs_indexHelp(item,L,left, mid-1)
    if L[mid]<item:
        return bs_indexHelp(item,L,mid+1,right) 
    
    return None
    



#return t or f 
def binary_search_iter(L, item):
    left = 0
    right = len(L)-1

    while right > left:
        mid = (right +left)//2
        if L[mid] == item:
            return True
        if L[mid] >item:
            right = mid -1
        if L[mid] < item:
            left = mid+1
    
    return False


def binary_search_recr(L, item):
    return bsHelp(L, item)
    
    
def bsHelp(L, item, left=0, right=None):   
    
    if right == None:
        right = len(L)-1
    
    if left > right:
        return False
    
    mid = (right +left)//2

    if L[mid] == item:
        return True
    if L[mid] >item:
        right = mid-1
        return bsHelp(L, item, left, right)
    if L[mid] < item:
        left = mid+1
        return bsHelp(L,item, left, right)
    
    return False


def bubblesort(L):
    unsorted = True
    while unsorted:
        unsorted = False
        for j in range(len(L)):
            for i in range(len(L)-1-j):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    unsorted = True


def selectionsort(L):
    for j in range(len(L)):
        minIndex = j
        for i in range(j+1,len(L)):
            if L[i] < L[minIndex]:
                minIndex = i
        L[j],L[minIndex] = L[minIndex], L[j]



def insertionsort(L):
   for i in range (1,len(L)):
       j=i
       while L[j-1]>L[j] and j>0:
           L[j-1],L[j]= L[j],L[j-1]
           j-=1




           



def quicksort(L):
    return quickHelp(L)

def quickHelp(L, left=0,right=None):
    if right == None:
        right = len(L)
    if right - left <=1:
        return None
    
    pivot_options = [L[0],L,[len(L)//2],L[-1]]
    pivot_options = sorted(pivot_options)
    pivot = pivot_options[1]

    i = left
    j= right-2

    while j>=i:
        if L[i]< pivot:
            i+=1
        if L[j]> pivot:
            j-=1
        if 
            


def mergesort(L):
    if len(L) < 2:
        return L
    
    left = mergesort(L[:len(L)//2])
    right = mergesort(L[len(L)//2:])
    merge(L, left, right)

    return L


def merge(L, left, right): 
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            L[i+j] = left[i]
            i+=1
        else:
            L[i+j] = right[j]
            j+=1
        
    L[i+j:] = left[i:] + right[j:]


   



print(reverse_string('abcd'))