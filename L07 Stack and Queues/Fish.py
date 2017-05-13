UP = 0
DOWN = 1
def solution(A, B):
    n = len(A)
    down = [0] * n
    down_len = 0
    alive = 0
    # first round
    for i in xrange(n):
        fish = (A[i], B[i])
        if fish[1] == UP and down_len == 0:
            alive += 1
        elif fish[1] == DOWN:
            down[down_len] = fish
            down_len += 1
        else: # fight
            while down_len != 0 and fish:
                if fish > down[down_len-1]:
                    down_len -= 1
                else:
                    fish = None
            if fish:
                alive += 1
    return alive + down_len

assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([4, 3], [0, 1 ])  == 2
assert solution([4, 3], [1, 0 ]) == 1
assert solution([3, 4], [0, 1 ]) == 2
assert solution([3, 4], [1, 0 ]) == 1

def solution2(A, B):
    alive = 0
    down = []
    for i in xrange(len(A)):
        if B[i] == 0 and not down: # upstream
            alive += 1
        elif B[i] == 0 and down: #fight
            while down and down[-1] < A[i]:
                down.pop()
            if not down:
                alive += 1
        else: # downstream
            down.append(A[i])
    return alive + len(down)