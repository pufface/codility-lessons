# coding=utf-8
'''
A non-empty zero-indexed array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''


def solution(A):
    candidate = None
    size = 0
    for a in A:
        if size == 0:
            candidate = a
            size += 1
        elif candidate != a:
            size -= 1
        else:
            size += 1
    if size <= 0:
        return 0
    left = 0
    right = sum([1 for a in A if a == candidate])
    len_A = len(A)
    count = 0
    for i, a in enumerate(A):
        if a == candidate:
            left += 1
            right -= 1
        if left > (i+1) // 2 and right > (len_A - 1 - i) // 2:
            count += 1
    return count

assert solution([4,3,4,4,4,2]) == 2
assert solution([1,1]) == 1
assert solution([1,1,1]) == 2
assert solution([4, 4, 2, 5, 3, 4, 4, 4]) == 3

def find_leader(A):
    value = 0
    size = 0
    for a in A:
        if size == 0 or value == a:
            size += 1
            value = a
        elif value != a:
            size -=1
    count = 0
    for a in A:
        if a == value:
            count += 1
    return value if count > len(A) / 2.0 else None

def solution2(A):
    leader = find_leader(A)
    if leader is None:
        return 0
    equi_leader = 0
    right = sum([1 for a in A if a == leader])
    left = 0
    for i, a in enumerate(A):
        if a == leader:
            left += 1
            right -= 1
        if (i+1) / 2.0 < left and (len(A)-i-1) / 2.0 < right:
            equi_leader += 1
    return equi_leader
