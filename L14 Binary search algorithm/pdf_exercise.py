'''
You are given n binary values x0, x1,... , xn-1, such that xi is from {0,1}. This array
represents holes in a roof (1 is a hole). You are also given k boards of the same size. The goal
is to choose the optimal (minimal) size of the boards that allows all the holes to be covered
by boards.
'''

# k - number of boards
# A - roof, 1 - hole
# find minimal size of boards covers all holes
def boards(A, k):
    n = len(A)
    beg = 1 # minimal size of board is 1
    end = n # maximal size of board is n
    result = -1
    while beg <= end:
        mid = (beg + end) / 2
        if num_boards(A, mid) <= k: # if we can cover all holes with less then k boards, we found one result, but has to keep going to find more optimal
            end = mid - 1
            result = mid
        else:
            beg = mid + 1
    return result

def num_boards(A, size):
    n = len(A)
    i = 0
    num_boards = 0
    while i < n:
        if A[i] == '1':
            num_boards += 1
            i += size
        else:
            i += 1
    return num_boards

assert boards(list('000011'), 2) == 1
assert boards(list('000011'), 1) == 2
assert boards(list('000011011'), 2) == 2