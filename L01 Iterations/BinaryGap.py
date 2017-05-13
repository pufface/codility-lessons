'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
'''


def solution(N):
    max_gap = 0
    gap = 0
    counting = False
    while N > 0:
        reminder = N % 2
        N /= 2
        if reminder == 0:
            gap += counting
        else:
            counting = True
            if gap > max_gap:
                max_gap = gap
            gap = 0
    return max_gap

assert(solution(5) == 1)
assert(solution(1041) == 5)
assert(solution(6) == 0)
assert(solution(328) == 2)

def solution1(N):
    gap = -1
    max_gap = 0
    while N > 0:
        if N % 2 == 1: #right bit is one
            max_gap = max(gap, max_gap)
            gap = 0
        elif gap != -1:
            gap += 1
        N /= 2
    return max_gap

def solution2(N):
    binary = bin(N)
    max_gap = 0
    gap = -1
    for digit in binary:
        if digit == '1':
            max_gap = max(gap, max_gap)
            gap = 0
        elif gap >= 0:
            gap += 1
    return max_gap
