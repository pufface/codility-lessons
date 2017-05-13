def caterpillar(A, s):
    n = len(A)
    front, total = 0, 0
    for back in xrange(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]
    return False

assert caterpillar([6,2,7,4,1,3,6], 12) == True

def solution(M, A):
    s = set()
    n = len(A)
    result = 0
    front = 0
    for back in A:
        while front < n and A[front] not in s:
            s.add(A[front])
            front += 1
            result += len(s)
        if back in s:
            s.remove(back)
    return min(result, 1000000000)

assert solution(6, [3,4,5,5,2]) == 9
assert solution(6, [1,2,3,4,5]) == 15
assert solution(6, [1,1,1,1,1]) == 5
assert solution(6, [1,2,1,2,1]) == 9
assert solution(6, [1,2,3,2,1]) == 11
assert solution(10, [1,3,9,10,1]) == 14
