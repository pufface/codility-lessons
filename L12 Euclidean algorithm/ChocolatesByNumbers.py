def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def solution(N, M):
    g = gcd(N, M)
    return N / g


assert solution(10, 4) == 5
