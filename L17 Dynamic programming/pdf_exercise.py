import sys

def dynamic_coin_change(C, amount):
    n = len(C)
    dp = [[0] * (amount+1) for _ in xrange(n+1)]
    dp[0] = [0] + [sys.maxint] * amount
    for i in xrange(1, n+1):
        denom = C[i-1]
        for price in xrange(1, denom):
            dp[i][price] = dp[i-1][price]
        for price in xrange(denom, amount+1):
            dp[i][price] = min(dp[i][price-denom] + 1, dp[i-1][price])
    return dp[-1]

def dynamic_coin_change2(C, amount):
    n = len(C)
    dp = [0] + [sys.maxint] * amount
    for i in xrange(1, n+1):
        denom = C[i-1]
        for price in xrange(denom, amount+1):
            dp[price] = min(dp[price-denom] + 1, dp[price])
    return dp

denominations = [1,3,4]
print dynamic_coin_change(denominations, 6)
print dynamic_coin_change2(denominations, 6)


'''
A small frog wants to get from position 0 to k (1 <= k <= 10000). The frog can
jump over any one of n fixed distances s0, s1,... , sn-1 (1 <= si <= k). The goal is to count the
number of different ways in which the frog can jump to position k. To avoid overflow, it is
sufficient to return the result modulo q, where q is a given number.
We assume that two patterns of jumps are different if, in one pattern, the frog visits
a position which is not visited in the other pattern.
'''

def frog(S, k):
    n = len(S)
    dp = [1] + [0] * k
    for i in xrange(n):
        jump = S[i]
        for pos in xrange(1,k+1):
            if jump <= pos:
                dp[pos] = dp[pos] + dp[pos-jump]
    return dp

S = [4,2]
k = 20
print frog(S, k)
