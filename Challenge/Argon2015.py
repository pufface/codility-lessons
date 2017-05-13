def can_seaside(num_seaside)

def solution(A):
    n = len(A)
    psum = [0] * (n + 1)
    first_seaside = -1
    last_mountain = -1
    for i in xrange(n):
        psum[i+1] = psum[i] + A[i]
        if A[i] == 0 and first_seaside == -1:
            first_seaside = i
        if A[i] == 1:
            last_mountain = i
    max_days = 0
    for i in xrange(1,n):
        # can seeside
        num_seaside = i+1 - (psum[i+1] - psum[0])
        if num_seaside > (i + 1 - first_seaside) / 2:


        num
        num_seaside = psum()

        max_days = max(days, max_days)
    return max_days1

assert solution([1, 1, 0, 1, 0, 0, 1, 1]) == 7
assert solution([1, 0]) == 0
