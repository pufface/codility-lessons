def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def has_same_prime_divisors(a, b):
    gcd_value = gcd(a,b)
    if a == b == 1:
        return True
    if gcd_value == 1:
        return False
    gcd_a = gcd_value
    while a / gcd_a != 1:
        a /= gcd_a
        gcd_a = gcd(a, gcd_value)
        if gcd_a == 1:
            return False
    gcd_b = gcd_value
    while b / gcd_b != 1:
        b /= gcd_b
        gcd_b = gcd(b, gcd_value)
        if gcd_b == 1:
            return False
    return True


def solution(P, Q):
    result = 0
    for i in xrange(len(P)):
        result += has_same_prime_divisors(P[i], Q[i])
    return result


assert solution([15,10,3],[75,30,5]) == 1
assert solution([1],[1]) == 1
assert solution([4],[64]) == 1
assert solution([4],[3]) == 0