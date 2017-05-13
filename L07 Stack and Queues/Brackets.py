'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''


brackets = {'(': 1, '{': 2, '[': 3, ')': 4, '}': 5, ']': 6}
def solution(S):
    stack = [0]*len(S)
    size = 0
    for s in S:
        value = brackets[s]
        if value <= 3:
            stack[size] = value
            size += 1
        elif stack[size-1]+3 == value:
            size -= 1
        else:
            return 0
    return int(size == 0)

assert(solution('{[()()]}') == 1)
assert(solution('([)()]') == 0)

left = "({["
right = ")}]"
def solution2(S):
    stack = []
    for letter in S:
        if letter in left:
            stack.append(left.index(letter))
        else:
            if stack and stack[-1] == right.index(letter):
                stack.pop()
            else:
                return 0
    return 1 if not stack else 0