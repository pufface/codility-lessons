def num_ways(n):
    n = float(n)
    return ((((1+5**0.5)/2)**n)-(((1-5**0.5)/2)**n))/5**0.5


def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in xrange(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


def solution(A, B):
    len_A = len(A)
    max_A = max(A)
    fib = fibonacci(max_A + 1)
    result = [0] * len_A
    for i in xrange(len_A):
        result[i] = fib[A[i]+1] % 2**B[i]
    return result

assert solution([4,4,5,5,1],[3,2,4,3,1]) == [5, 1, 8, 0, 1]
