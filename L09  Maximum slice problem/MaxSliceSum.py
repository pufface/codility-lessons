def solution(A):
    n = len(A)
    max_ending = A[0]
    max_sum = max_ending
    for i in xrange(1,n):
        max_ending = max(A[i], max_ending+A[i])
        max_sum = max(max_ending, max_sum)
    return max_sum


assert solution([3, 2, -6, 4, 0]) == 5
