def factorial(n):
    """Returns the nth factorial"""
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
    
x = factorial(4)
print(x)