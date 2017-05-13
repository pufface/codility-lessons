# coding=utf-8
"""
Write a function:

def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


def solution(A):
    n = len(A)
    t = [0]*n
    for x in A:
        if 1 <= x <= n:
            t[x-1] = 1
    for i,x in enumerate(t):
        if x == 0:
            return i+1
    return n + 1

assert solution([1,3,6,4,1,2]) == 5
assert solution([3]) == 1
assert solution([1]) == 2
assert solution([0]) == 1
assert solution([-1]) == 1
assert solution([2,3,4]) == 1
assert solution([1,2,4]) == 3
assert solution([5,6,7]) == 1

def solution2(A):
    n = len(A)
    counter = [0] * (n+1)
    for a in A:
        if 0 <= a <= n:
            counter[a] += 1
    for i in xrange(1,n+1):
        if counter[i] == 0:
            return i
    return n + 1