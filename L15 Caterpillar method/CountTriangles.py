def solution(A):
    n = len(A)
    A.sort()
    # A[i+2] + A[i+i] > A[i]
    # A[i+2] + A[i] > A[i+i]
    # A[i+1] + A[i} > A[i+2] ???
    result = 0
    for first in xrange(0, n-2):
        third = first + 2
        for second in xrange(first+1, n-1):
            while third < n and A[second] + A[first] > A[third]:
                third += 1
            result += third - second - 1
    return result

assert solution([10,2,5,1,8,12]) == 4
