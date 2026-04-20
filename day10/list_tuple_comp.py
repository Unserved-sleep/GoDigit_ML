from sys import getsizeof
from timeit import timeit

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
print(getsizeof(tup))
print(getsizeof(lst))
print(timeit(stmt= lambda : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), number=10000))
print(timeit(stmt= lambda : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], number=10000))
print(timeit(stmt= lambda : list(tup), number=10000))
print(timeit(stmt= lambda : tuple(lst), number=10000))