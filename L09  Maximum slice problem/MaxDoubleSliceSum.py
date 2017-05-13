# Maximum subarray problem


def solution(A):
    n = len(A)
    prefix = [0] * n
    suffix = [0] * n
    for i in xrange(1, n-1):
        prefix[i] = max(0, prefix[i-1] + A[i])
    for i in xrange(n-2, 0, -1):
        suffix[i] = max(0, suffix[i+1] + A[i])
    max_slice = 0
    for i in xrange(1, n-1):
         double_slice = prefix[i-1] + suffix[i+1]
         if double_slice > max_slice:
             max_slice = double_slice
    return max_slice

assert solution([5, 17, 0, 3]) == 17
assert solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17
assert solution([5,5,5]) == 0


