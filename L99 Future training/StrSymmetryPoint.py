def solution(S):
    n = len(S)
    if n % 2 == 0:
        return -1
    for i in xrange(n/2):
        if S[i] != S[-i-1]:
            return -1
    return n/2


assert solution("racecar") == 3
assert solution("x") == 0
assert solution("") == -1
assert solution("xy") == -1

