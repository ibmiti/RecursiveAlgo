# def fibonacci (n):
#     if n == 1:
#         return 1
#     elif n ==2:
#         return 1
#     elif n > 2:
#         return fibonacci(n - 1) + fibonacci(n-2)
#
# for n in range(1, 101):
#     print(n, ":",  fibonacci(n))
#


# this is a recursive function

 # we will compute the value, store it and then return it
# fibonacci_cache = {}
#
# def fibonacci(n):
#     #if we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     # Compute the Nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
# # cache the value and return it
# fibonacci_cache[n] = value
# return value
#
# for n in range(1,1001):
#     print(n, ":", fibonacci(n))


# this next alg will be the most efficient


from functools import lru_cache
#lru stands for last recently used cache ,, the line above provides a one line way to add memoization to function

@lru_cache(maxsize = 1000)
def fibonacci(n):
    #check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
        
    # compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print(n, ":", fibonacci(n))
