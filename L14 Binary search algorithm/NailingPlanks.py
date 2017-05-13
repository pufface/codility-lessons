inf = float('inf')

def find_first_nail(plank_start, plank_end, nails):
    # left boundery
    left_boundary = None
    beg = 0
    end = len(nails) - 1
    while beg <= end:
        mid = (beg+end + 1) / 2
        if nails[mid][1] < plank_start:
            beg = mid + 1
        else:
            left_boundary = mid
            end = mid - 1
    if left_boundary is None:
        return -1
    # right boundary
    right_boundary = None
    beg = left_boundary
    end = len(nails) - 1
    while beg <= end:
        mid = (beg+end) / 2
        if nails[mid][1] > plank_end:
            end = mid - 1
        else:
            beg = mid + 1
            right_boundary = mid
    if right_boundary is None:
        return -1
    pos = inf
    for i in xrange(left_boundary, right_boundary +1):
        if plank_start <= nails[i][1] <= plank_end:
            pos = min(pos, nails[i][0])
    if pos == inf:
        return -1
    return pos

def solution(A, B, C):
    C = sorted(enumerate(C), key = lambda x : x[1])
    result = -1
    for i in xrange(len(A)):
        first_nail_pos = find_first_nail(A[i],B[i],C)
        if first_nail_pos == -1:
            return -1
        result = max(first_nail_pos, result)
    return result + 1

assert solution([1,4,5,8],[4,5,9,10],[4,6,7,10,2]) == 4
assert solution([1], [2], [2,2,2]) == 1
assert solution([1], [1], [2]) == -1
#