def solution(A):
    rightsum = sum(A)
    leftsum = 0
    n = len(A)
    for i in xrange(n):
        val = A[i]
        rightsum -= val
        if leftsum == rightsum:
            return i
        leftsum += val
    return -1

assert solution([-1, 3, -4, 5, 1, -6, 2, 1]) in {1,3,7}