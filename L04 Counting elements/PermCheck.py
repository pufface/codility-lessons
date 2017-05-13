
"""
A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


def solution(A):
    n = len(A)
    t = [0]*n
    for x in A:
        if not 1 <= x <= n:
            return 0
        if t[x-1] != 0:
            return 0
        else:
            t[x-1] = 1
    return 1

assert solution([4,1,3,2]) == 1
assert solution([4,2,2,2]) == 0
assert solution([4,1,3]) == 0

def solution2(A):
    n = len(A)
    count = [0] * (n+1)
    unique = 0
    for a in A:
        if a <= 0 or a > n:
            return 0
        count[a] += 1
        if count[a] == 1:
            unique += 1
        else:
            return 0
    return 1 if unique == n else 0