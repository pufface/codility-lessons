neg_inf = -float('inf')

def solution(A):
    n = len(A)
    dp = [neg_inf] * n
    dp[0] = A[0]
    for i in xrange(n):
        for x in xrange(1,7):
            if i+x >= n:
                break
            dp[i+x] = max(dp[i+x], dp[i] + A[i+x])
    return dp[-1]

assert solution([1,-2,0,9,-1,-2]) == 8
