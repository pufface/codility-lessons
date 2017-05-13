def solution_slow(A):
    n = len(A)
    result = 0
    for p in xrange(n):
        for q in xrange(p+1,n):
            if A[q] < A[p]:
                result += 1
    print result
    return min(result,  1000000000)

def bs(a, C):
    beg = 0
    end = len(C)-1
    result = -1
    while beg <= end:
        mid = (beg+end) / 2
        if a > C[mid]:
            result = mid
            beg = mid + 1
        else:
            end = mid - 1
    return result



def solution(A):
    C = sorted(A)
    result = 0
    for a in A:
        print C
        pos_before = bs(a,C)
        del C[pos_before+1]
        result += pos_before + 1
        if result > 1000000000:
            return -1
    return result


assert solution([-1, 6, 3, 4, 7, 4] ) == 4