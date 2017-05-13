def solution(K, A):
    rope_sum = 0
    counter = 0
    for a in A:
        rope_sum += a
        if rope_sum >= K:
            counter += 1
            rope_sum = 0
    return counter

assert solution(4, [1,2,3,4,1,1,3]) == 3
