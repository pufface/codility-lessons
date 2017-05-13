'''
maximal sum of sub-slice
'''

# can contain empty elements
def max_slice_empty(A):
    maxslice = maxend = 0
    for a in A:
        maxend = max(maxend + a, 0)
        maxslice = max(maxslice, maxend)
    return maxslice

# must contain at least one element
def max_slice(A):
    maxslice = maxend = A[0]
    for a in A[1:]:
        maxend = max(maxend + a, a)
        maxslice = max(maxslice, maxend)
    return maxslice

assert max_slice_empty([5,-7,3,5,-2,4,-1]) == 10
assert max_slice([5,-7,3,5,-2,4,-1]) == 10
assert max_slice([-7,-3,-1]) == -1