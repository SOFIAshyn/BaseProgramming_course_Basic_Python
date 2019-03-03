# def fib_rec(n):
#
#
# def fib_iter(n):
#     sum = 0
#
#     for i in range(n):
#         if i <= 1:
#             prev = 1
#             pre
#         prev =
#         sum += prev + prev_prev
#
# def numbers_time_test():
#     pass
#
#
# if __name__ == "__main__":

# def fib(n, depth=0):
#     print(" "*depth, "fib(", n, ")")
#     if (n < 2):
#         result = 1
#     else:
#         result = fib(n-1, depth+1) + fib(n-2, depth+1)
#         print(" "*depth, "-->", result)
#     return result
#

# def fib(n, depth=0):
#     print("     " * depth, "fib(", n, ")")
#     if n < 2:
#         result = 1
#     else:
#         result = fib(n - 1) + fib(n - 2)
#     print("     " * depth, "-->", result)
#     return result
#
# print(fib(5))
import timeit
from functools import lru_cache

@lru_cache(maxsize=1000)
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)




print(fib_rec(40))

if __name__ == "__main__":
    time = timeit.default_timer()
    fib_rec()