# coding=utf-8
'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

int solution(int A[], int N);

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''


# solution inspired by http://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
def solution(A):
    result = 0
    len_A = len(A)
    disk_start = [0]*len_A
    disk_end = [0]*len_A
    for i, disk in enumerate(A):
        disk_start[max(0, i - disk)] += 1
        disk_end[min(len_A-1, i + disk)] += 1
    num_active = 0
    for i in xrange(len_A):
        # num of k-combinations = (n*(n-1)*..*(n-k+1)) / (k*(k-1)*..*1)
        # num of 2-combinations = (n*n-1) / 2
        # in one point n disk start there must be intersection which each other, so 2-combination of n
        result += disk_start[i] * (disk_start[i] - 1) / 2
        # every new disk add number of active disk intersections
        result += num_active * disk_start[i]
        num_active += disk_start[i]
        num_active -= disk_end[i]
        if (result > 10000000):
            return -1
    return result

assert(solution([1,1]) == 1)
assert(solution([1,5,2,1,4,0]) == 11)

def solution2(A):
    len_A = len(A)
    counter = 0
    for i in xrange(0, len_A):
        for x in xrange(i+1, len_A):
            if i + A[i] >= x - A[x]:
                counter += 1
    return counter

assert(solution2([1,1]) == 1)
assert(solution2([1,5,2,1,4,0]) == 11)

def solution3(A):
    n = len(A)
    disk = [0] * n
    for i in xrange(n):
        disk[i] = (i - A[i], i + A[i])
    print disk
    print sorted(disk)

# assert(solution3([1,1]) == 1)
assert(solution3([1,5,2,1,4,0]) == 11)