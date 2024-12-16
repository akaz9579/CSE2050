from fib import fib, fib_memo
import timeit

SETUP_Code = '''
from __main__ import k, fib, fib_memo
'''

STMT_fib = '''
fib(k)
'''

STMT_fib_memo = '''
fib_memo(k)
'''


UNIT_FACTOR = 1E6 # Microseconds scalar
# Table Header
print("Total time in us to run each operation 10 times.")
print('='*80)

print(f"{'k':6}{'fib':10}{'fib_memo':10}")
print('-'*80)

for i in range(1, 30):
    k = i*1
    # Add First
    t_fib = UNIT_FACTOR*timeit.timeit(setup=SETUP_Code, stmt=STMT_fib, number=10)
    t_fib_memo = UNIT_FACTOR*timeit.timeit(setup=SETUP_Code,stmt=STMT_fib_memo, number=10)
   
    print(f"{k:<6}{t_fib:<10.3g}{t_fib_memo:<10.3g}")