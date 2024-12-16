import timeit

# def sum_k(k):
#     """Returns the nth factorial"""
#     return (k/2)*(k+1)

# if __name__ == '__main__':
#     sols = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45, 10:55}

#     for key in sols:
#         assert sum_k(key) == sols[key]

def sumk_recr(k):
    if k == 1:
        return 1
    return k + sumk_recr(k-1)
# O(n) memory overhead

def sumk_iter(k):
    temp_sum = 1
    for i in range(2, k+1):
        temp_sum += i
    return temp_sum
# O(1) memory overhead

for k in range(1,100): assert sumk_recr(k) == sumk_iter(k)

for func in [sumk_recr, sumk_iter]:
    t = timeit.timeit(f'{func.__name__}(40)', globals=globals())
    print(f"{func.__name__}: {t:.3g} s")