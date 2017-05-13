# coding=utf-8
'''
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by a zero-indexed array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given a zero-indexed array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Assume that:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''


def solution(H):
    result = 0
    stack = [-1]*len(H)
    size = 0
    for height in H:
        while size > 0 and stack[size-1] > height:
            size -= 1
        if size == 0 or stack[size-1] < height:
            result += 1
            stack[size] = height
            size += 1
    return result

assert(solution([8,8,5,7,9,8,7,4,8]) == 7)
assert(solution([2, 3, 2, 1]) == 3)

def solution2(H):
    stack = []
    count = 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
            count += 1
        if not stack or stack[-1] < h:
            stack.append(h)
    return count + len(stack)