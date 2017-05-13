def solution(N):
    min_len = float('inf')
    for i in xrange(1, int(N**0.5) + 1):
        if N % i == 0:
            length = 2 * (i + N / i)
            min_len = min(min_len, length)
    return min_len

assert solution(30) == 22

def solution2(n):
    i = 1
    min_perimeter = float('inf')
    while i * i <= n:
        if n % i == 0:
            a = i
            b = n / i
            min_perimeter = min(min_perimeter, 2*(a+b))
        i += 1
    return min_perimeter