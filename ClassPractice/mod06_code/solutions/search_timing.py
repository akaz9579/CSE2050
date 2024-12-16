from searches import linear_search, binary_search_slice, binary_search_recr, binary_search_iter
import timeit

SETUP_Code = '''
from __main__ import n, L, linear_search, binary_search_slice, binary_search_recr, binary_search_iter
'''

STMT_ls = '''
linear_search(-1, L)
'''
STMT_bss = '''
binary_search_slice(-1, L)
'''

STMT_bsr = '''
binary_search_recr(-1, L)
'''

STMT_bsi = '''
binary_search_iter(-1, L)
'''




UNIT_FACTOR = 1E6 # Microseconds scalar
COLUMN_WIDTH = 12
# Table Header
print("Total time in us to search for an item not in the list")
print('='*46)

print(f"{'k':6}{'lin':<12}{'recr slice':<12}{'recr idx':<12}{'iter':<12}")
print('-'*46)

for i in range(1, 10):
    n = i*10000
    L = [i for i in range(n)]
      
    # Add First
    print(f"{n:<6}", end='')
    for STMT in [STMT_ls, STMT_bss, STMT_bsr, STMT_bsi]:
        t = UNIT_FACTOR*timeit.timeit(setup=SETUP_Code, stmt=STMT, number=1)
        print(f"{t:<12.3g}", end='')
    print()