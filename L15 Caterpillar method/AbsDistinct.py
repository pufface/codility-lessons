# O(n log(n))
def solution(A):
    s = set()
    for a in A:
        s.add(abs(a))
    return len(s)

# O(n)
def solution(A):
    left = 0
    right = len(A) - 1
    count_distinct = 0
    while left <= right:
        l = abs(A[left])
        r = abs(A[right])
        if l > r:
            left += 1
            while left <= right and abs(A[left]) == l:
                left += 1
            count_distinct += 1
        elif r > l:
            right -= 1
            while left <= right and abs(A[right]) == r:
                right -= 1
            count_distinct += 1
        else:
            left += 1
            while left <= right and abs(A[left]) == l:
                left += 1
            right -= 1
            while left <= right and abs(A[right]) == r:
                right -= 1
            count_distinct += 1
    return count_distinct

assert solution([1,1,1]) == 1
assert solution([1]) == 1
assert solution([1, 2, 2]) == 2
assert solution([1, 1, 2]) == 2
assert solution([-5,-3,-1,0,3,6]) == 5
