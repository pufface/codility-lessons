
#  store array with primes from 0 to N-1
#  n*log(log(n))
def primes(n):
    sieves = [True] * (n+1)
    sieves[0] = sieves[1] = False
    i = 2
    while i * i <= n:
        if sieves[i]:
            k = i * i
            while k <= n:
                sieves[k] = False
                k += i
        i += 1
    return sieves
#
# p = primes(30)
# for i in xrange(30):
#     if p[i]:
#         print i

# store array with primes == 0, non_primes == smallest prime divisor
def factorization(n):
    F = [0] * (n+1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

print factorization(26)

def solution(N, P, Q):
    F = factorization(N)
    len_F = len(F)
    S = [0]*len_F
    for i in xrange(1, len_F):
        S[i] = S[i-1] + int(F[i] != 0 and F[i / F[i]] == 0)
    len_P = len(P)
    result = [0]*len_P
    for i in xrange(len_P):
        result[i] = max(0, S[Q[i]] - S[P[i]-1])
    return result

assert solution(26, [1,4,16], [26, 10, 10]) == [10, 4, 0]


def factorization(n):
    sieve = [0] * n
    i = 2
    while i * i < n:
        if sieve[i] == 0:
            k = i*i
            while k < n:
                if sieve[k] == 0:
                    sieve[k] = i
                k += i
        i += 1
    return sieve

def prefix_semiprimes(sieves):
    n = len(sieves)
    prefix = [0] * (n+1)
    for i in xrange(1,n+1):
        d = sieves[i-1]
        prefix[i] = prefix[i-1] + int(d and sieves[i / d] == 0)
    return prefix

def solution(N, P, Q):
    prefix = prefix_semiprimes(factorization(N+1))
    n = len(P)
    ans = [0] * n
    for i in xrange(n):
        ans[i] = prefix[Q[i]+1] - prefix[P[i]]
    return ans
