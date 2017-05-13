def solution(A):
    A.sort()
    left, right = 0, len(A) - 1
    m = float('inf')
    while left <= right:
        s = A[left] + A[right]
        m = min(abs(s), m)
        if s > 0:
            right -= 1
        else:
            left += 1
    return m

assert solution([1,4,-3]) == 1
assert solution([-8,4,5,-10,3]) == 3
