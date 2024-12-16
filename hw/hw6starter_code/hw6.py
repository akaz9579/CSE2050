

def bubble_sort(matrix):
    """Sorts the first row of the matrix"""
    n = len(matrix[0])
    n_swaps = 0
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if matrix[0][j] > matrix[0][j + 1]:
                matrix[0][j], matrix[0][j + 1] = matrix[0][j + 1], matrix[0][j]
                n_swaps += 1
                swapped = True
        if not swapped:
            break
    return matrix[0], n_swaps

def insertion_sort(matrix):
    """Sorts the second row of the matrix using insertion sort"""
    n = len(matrix[1])
    n_swaps = 0
    for i in range(1, n):
        key = matrix[1][i]
        j = i - 1
        while j >= 0 and matrix[1][j] > key:
            matrix[1][j + 1] = matrix[1][j]
            j -= 1
            n_swaps += 1
        matrix[1][j + 1] = key
    return matrix[1], n_swaps

def selection_sort(matrix):
    """Sorts the third row of the matrix using selection sort"""
    n = len(matrix[2])
    n_swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if matrix[2][j] < matrix[2][min_idx]:
                min_idx = j
        if min_idx != i:
            matrix[2][i], matrix[2][min_idx] = matrix[2][min_idx], matrix[2][i]
            n_swaps += 1
    return matrix[2], n_swaps

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list


matrix = [
        [10, 2, 3, 8, 1],    # First row (Bubble Sort)
        [7, 15, 14, 20, 9],  # Second row (Insertion Sort)
        [25, 12, 5, 3, 16]   # Third row (Selection Sort)
        ]


# Step 1: Sort the first row using Bubble Sort
sorted_1_bubble, bubble_swaps = bubble_sort(matrix)
print("After Bubble Sort:", sorted_1_bubble, "Swaps:", bubble_swaps)

# Step 2: Sort the second row using Insertion Sort
sorted_2_insertion, insertion_swaps = insertion_sort(matrix)
print("After Insertion Sort:", sorted_2_insertion, "Swaps:", insertion_swaps)

# Step 3: Sort the third row using Selection Sort
sorted_3_selection, selection_swaps = selection_sort(matrix)
print("After Selection Sort:", sorted_3_selection, "Swaps:", selection_swaps)

# Step 4: Merge the sorted rows into one sorted list
merged_list = merge(sorted_1_bubble, sorted_2_insertion, sorted_3_selection)
print("Merged List:", merged_list)