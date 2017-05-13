def solution(A):
    n = len(A)
    next_peaks = []
    for i in xrange(1,n-1):
        left = A[i-1]
        center = A[i]
        right = A[i+1]
        is_peak = left < center > right
        if is_peak:
            next_peaks.append(i)
    len_next = len(next_peaks)
    if len_next == 0:
        return 0
    max_k = 0
    k = 1
    max_posible = next_peaks[-1] - next_peaks[0]
    while (k - 1) * k <= max_posible:
        count = 1
        previous_pos = next_peaks[0]
        for i in xrange(1,len_next):
            if next_peaks[i] - previous_pos >= k:
                previous_pos = next_peaks[i]
                count += 1
                if count >= k:
                    break
        if count >= k:
            max_k = max(max_k, k)
        k += 1
    return max_k


assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
assert solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1]) == 2
assert solution([5]) == 0
assert solution([1,3,2]) == 1

def peaks_position(A):
    n = len(A)
    if n < 2:
        return []
    peaks = []
    for i in xrange(1,n-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    return peaks

def can_flags(peaks, flags):
    prev = None
    count = 0
    for peak in peaks:
        if prev is None or peak - prev >= flags:
            prev = peak
            count += 1
            if count >= flags:
                break
    return count >= flags


def solution(A):
    peaks = peaks_position(A)
    n = len(peaks)
    if n <= 1:
        return n
    max_length = peaks[-1] - peaks[0]
    max_flags = 0
    i = 1
    while i * (i-1) <= max_length:
        if can_flags(peaks, i):
            max_flags = max(max_flags, i)
        i += 1
    return max_flags