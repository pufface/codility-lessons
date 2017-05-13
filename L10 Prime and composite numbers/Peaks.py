def solution(A):
    n = len(A)
    if n < 3:
        return 0
    prefix_peaks = [0] * (n+1)
    for i in xrange(0, n-2):
        left = A[i]
        peek = A[i+1]
        right = A[i+2]
        prefix_peaks[i+2] = prefix_peaks[i+1] + int(left < peek > right)
    prefix_peaks[i+3] = prefix_peaks[i+2] + 0
    max_num_block = 0
    candidate = 1
    while candidate * candidate <= n:
        if n % candidate == 0:
            num_block, block_size = candidate, n / candidate
            for block in xrange(num_block):
                block_start = block*block_size
                block_end = block_start + block_size
                block_peaks = prefix_peaks[block_end] - prefix_peaks[block_start]
                if block_peaks == 0:
                    break
            else:
                max_num_block = max(max_num_block, num_block)

            if block_size != num_block:
                block_size, num_block = num_block, block_size
                for block in xrange(num_block):
                    block_start = block*block_size
                    block_end = block_start + block_size
                    block_peaks = prefix_peaks[block_end] - prefix_peaks[block_start]
                    if block_peaks == 0:
                        break
                else:
                    max_num_block = max(max_num_block, num_block)
        candidate += 1
    return max_num_block


assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
assert solution([5]) == 0
assert solution([1, 3, 2, 1]) == 1
assert solution([1, 2, 3, 4, 5, 6]) == 0
assert solution([0, 1, 0, 0, 0]) == 1
assert solution([0, 1, 0, 1, 0]) == 1
assert solution([0, 1, 0, 1, 0, 1]) == 2


def get_factors(n):
    factors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n/i)
        i += 1
    return factors

def prefix_peaks(A):
    n = len(A)
    prefix = [0] * (n+1)
    for i in xrange(1,n-1):
        is_peak = A[i-1] < A[i] > A[i+1]
        prefix[i+1] = prefix[i] + int(is_peak)
    prefix[i+2] = prefix[i+1]
    return prefix

def block_has_peak(prefix, block_size, num_block):
    for i in xrange(0, num_block):
        if prefix[(i+1) * block_size] - prefix[i*block_size] == 0:
            return False
    return True

def solution(A):
    n = len(A)
    if n <= 2:
        return 0
    max_block = 0
    prefix = prefix_peaks(A)
    for factor in get_factors(n):
        block_size = factor
        num_block = n / factor
        if block_has_peak(prefix, block_size, num_block):
            max_block = max(max_block, num_block)
    return max_block
