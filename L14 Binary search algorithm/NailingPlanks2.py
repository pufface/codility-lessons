# uncomplete
def check(A, B, C):
    max_len = B[-1]
    nails_pos = [0] * (max_len + 1)
    for c in C:
        if c < len(nails_pos):
            nails_pos[c] = 1
    nails_pos_prefix = [0] * (len(nails_pos) + 1)
    for i in xrange(len(nails_pos)):
        nails_pos_prefix[i+1] = nails_pos_prefix[i] + nails_pos[i]
    for i in xrange(len(A)):
        num_nails_in_plank = nails_pos_prefix[B[i]+1] - nails_pos_prefix[A[i]]
        if num_nails_in_plank == 0:
            return False
    return True


def solution(A, B, C):
    result = -2
    beg = 0
    end = len(C) -1
    while beg <= end:
        mid = (beg + end) / 2
        if check(A, B, C[0:mid+1]):
            result = mid
            end = mid - 1
        else:
            beg = mid + 1
    return result + 1

assert solution([1,4,5,8],[4,5,9,10],[4,6,7,10,2]) == 4
assert solution([1], [2], [2,2,2]) == 1
assert solution([1], [1], [2]) == -1
#