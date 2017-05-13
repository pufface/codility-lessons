def fibonacci(n, max_value):
    d = {}
    fib_prev_prev = 0
    fib_prev = 1
    fib = 0
    while True:
        fib = fib_prev + fib_prev_prev
        d[fib] = 1
        fib_prev, fib_prev_prev = fib, fib_prev
        if fib > max_value:
            break
    return d


def solution(A):
    len_A = len(A)
    fib_dict = fibonacci(len_A + 1, len_A)
    jumps = 1
    last_jump_position = set()
    last_jump_position.add(-1)
    while True:
        next_jump_position = set()
        for last_jump in last_jump_position:
            for i in xrange(last_jump+1, len_A+1):
                can_jump = True if i == len_A or A[i] else False
                if can_jump and fib_dict.get(i-last_jump, 0):
                    if i == len_A:
                        return jumps
                    elif i not in last_jump_position:
                        next_jump_position.add(i)
        jumps += 1
        if not next_jump_position:
            return -1
        last_jump_position = next_jump_position

assert solution([0,0,0,1,1,0,1,0,0,0,0]) == 3
assert solution([]) == 1
assert solution([1]) == 1
