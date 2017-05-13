'''
You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, ..., an-1 and b0, b1, ..., bn-1 respectively (0 <= ai, bi <= m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and one element from array B and exchanging them
'''

def counting(A):
    d = {}
    for a in A:
        d[a] = d.get(a, 0) + 1
    return d

def solution(A,B):
    suma = sum(A)
    sumb = sum(B)
    m = max(A)
    diff = sumb - suma
    if diff % 2 == 1:
        return False
    diff //= 2
    d = counting(A)
    # looking for suma - diff == sumb + diff
    n = len(A)
    for i in xrange(n):
        if 0 <= B[i]-diff <= m and d.get(B[i]-diff) > 0:
            return True
    return False

assert solution([1,2], [1,2]) == True
assert solution([1,1], [2,2]) == True
assert solution([1,2], [2,3]) == True
assert solution([1,2], [1,3]) == False