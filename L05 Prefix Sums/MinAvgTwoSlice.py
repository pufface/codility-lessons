# coding=utf-8

"""
A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

int solution(int A[], int N);

that, given a non-empty zero-indexed array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


def solution(A):
    min_avg_value = (A[0] + A[1]) / 2.0
    min_avg_pos = 0
    for index in range(0, len(A)-2):
        # Try the next 2-element slice
        avg2 = (A[index] + A[index+1]) / 2.0
        if avg2 < min_avg_value:
            min_avg_value = avg2
            min_avg_pos = index
        # Try the next 3-element slice
        avg3 = (A[index] + A[index+1] + A[index+2]) / 3.0
        if avg3 < min_avg_value:
            min_avg_value = avg3
            min_avg_pos = index
    # Try the last 2-element slice
    avg2 = (A[-1] + A[-2]) / 2.0
    if avg2 < min_avg_value:
        min_avg_value = avg2
        min_avg_pos = len(A)-2
    return min_avg_pos

assert solution([4, 2, 2, 5, 1, 5, 8]) == 1

'''
(1) There must be some slices, with length of two or three, having the minimal average value among all the slices.
(2) And all the longer slices with minimal average are built up with these 2-element and/or 3-element small slices.
https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility
'''
def solution2(A):
    min_avg = (A[0] + A[1]) / 2.0
    min_pos = 0
    for i in xrange(1, len(A) - 1):
        two_slice_min = (A[i] + A[i+1]) / 2.0
        if two_slice_min < min_avg:
            min_avg = two_slice_min
            min_pos = i
    for i in xrange(0, len(A) - 2):
        three_slice_min = (A[i] + A[i+1] + A[i+2]) / 3.0
        if three_slice_min < min_avg:
            min_avg = three_slice_min
            min_pos = i
    return min_pos