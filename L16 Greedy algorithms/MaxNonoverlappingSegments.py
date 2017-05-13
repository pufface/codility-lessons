def solution(A, B):
    n = len(A)
    if n == 0:
        return 0
    seg_end = [B[0]]
    for i in xrange(1, n):
        if not A[i] <= seg_end[-1] <= B[i]:
            seg_end.append(B[i])
    return len(seg_end)


assert solution([1,3,7,9,9],[5,6,8,9,10]) == 3
