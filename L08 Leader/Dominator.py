# coding=utf-8
'''
A zero-indexed array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given a zero-indexed array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
For example, given array A such that

A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''


# remove two different elements from array dominator remain same
# two different elements is removed by stack, elements in stack are same so no need remember all values, just top and size
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
        return -1
    count = 0
    idx = None
    for i, a in enumerate(A):
        if a == candidate:
            count += 1
            idx = i
    return idx if count > len(A) // 2 else -1

assert solution([3, 4, 3, 2, 3, -1, 3, 3]) in [0, 2, 4, 6, 7]
assert solution([1,1,3, 3, 3]) in [0, 2, 4, 6, 7]

def solution2(A):
    value = 0
    size = 0
    for a in A:
        if size == 0 or value == a:
            value = a
            size += 1
        elif value != a:
            size -= 1
    if size == 0:
        return -1
    count = 0
    for a in A:
        if a == value:
            count +=1
    return A.index(value) if count > len(A) / 2.0 else -1