'''
Let's check whether a sequence a0, a1,... ,an-1 (1 <= ai <=10^9) contains a contiguous subsequence
whose sum of elements equals s.
'''

def caterpillar(A, s):
    n = len(A)
    front = 0
    summary = 0
    for tail in xrange(n):
        while front < n and summary <= s:
            summary += A[front]
            front += 1
            if summary == s:
                return True
        summary -= A[tail]
    return False


print caterpillar([6,2,7,4,1,3,6], 12)
print caterpillar([6], 6)


'''
You are given n sticks (of lengths 1 <= a0 <= a1  <= ... <= an-1 <= 10^9). The goal is
to count the number of triangles that can be constructed using these sticks. More precisely,
we have to count the number of triplets at indices x < y < z, such that a[x] + a[y] > a[z].
'''

def triangels(A):
    n = len(A)
    count = 0
    for x in xrange(n):
        z = x + 2
        for y in xrange(x+1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            count += z - y - 1
    return count

# ONE triangle is possible namely (3,6,7)
print triangels([1,3,6,7])
# THREE triangle is possible namely (2,3,4), (2,4,5), (3,4,5)
print triangels([2,3,4,5])