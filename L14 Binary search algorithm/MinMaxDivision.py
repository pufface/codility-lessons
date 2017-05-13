def max_num_block(A, max_block_size):
    num = 0
    block_sum = 0
    for a in A:
        if block_sum + a > max_block_size:
            block_sum = a
            num += 1
        else:
            block_sum += a
    return num + int(block_sum != 0)


def solution(K, M, A):
    result = 0
    lower_sum = max(A)
    upper_sum = sum(A)
    if K == 1:
        return upper_sum
    if K >= len(A):
        return lower_sum
    while lower_sum <= upper_sum:
        mid_sum = (lower_sum + upper_sum) / 2
        min_blocks_needed = max_num_block(A, mid_sum)
        if min_blocks_needed <= K:
            result = mid_sum
            upper_sum = mid_sum - 1
        else:
            lower_sum = mid_sum + 1
    return result

assert solution(3, 5, [2,1,5,1,2,2,2],) == 6
