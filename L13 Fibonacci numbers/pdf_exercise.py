'''
For all the given numbers x0, x1,... ,xn-1, such that 1 <= xi <= m <= 1 000 000,
check whether they may be presented as the sum of two Fibonacci numbers.
'''

def fibonacci(n):
    fb = [0] * n
    fb[1] = 1
    for i in xrange(2,n):
        fb[i] = fb[i-1] + fb[i-2]
    return fb

def check_sum_two_fibonacci(k):
    fb = fibonacci(31)
    d = set(fb)
    i = 1
    while i < len(fb) and fb[i] < k:
        if k-fb[i] in d:
            return True
        i += 1
    return False

print check_sum_two_fibonacci(26) # TRUE 21 + 5
print check_sum_two_fibonacci(33) # FALSE
print check_sum_two_fibonacci(4) # TRUE 3 + 1
print fibonacci(31)