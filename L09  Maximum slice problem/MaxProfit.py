def solution(A):
    n = len(A)
    if n < 2:
        return 0
    diff = A[1] - A[0]
    max_profit = max(0, diff)
    for i in xrange(1, n - 1):
        next_diff = A[i+1] - A[i]
        diff = max(next_diff, diff + next_diff)
        max_profit = max(max_profit, diff)
    return max_profit

assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356

def solution2(A):
    n = len(A)
    if n < 2:
        return 0
    diff = 0
    max_diff = 0
    for i in xrange(1,n):
        new_diff = A[i] - A[i-1]
        diff = max(new_diff, new_diff + diff)
        max_diff = max(diff, max_diff)
    return max_diff