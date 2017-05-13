
def subarray_sum(A):
    S = sum(A)
    dp = [0] * (S+1)
    # sum of empty sub-array is possible
    dp[0] = 1
    for a in A:
        # reverse order ensures that element is counted only once
        for s in xrange(S, -1, -1):
            if dp[s] and s + a <= S:
                dp[s+a] = 1
    return dp

def solution(A):
    # key is find to arrays P, Q with minimal difference between their sums
    A = map(abs, A)
    # find all possible sum of every subarray
    dp = subarray_sum(A)
    # find maximal sum of subbray which is less or equal sum(A)/2
    sum_A = sum(A)
    sum_P = 0
    print dp
    for i in xrange(sum_A / 2, -1, -1):
        if dp[i] == 1:
            sum_P = i
            break
    sum_Q = sum_A - sum_P
    return abs(sum_Q - sum_P)

assert solution([1,5,2,-2]) == 0
