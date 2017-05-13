def soluotion(N):
    i = 1
    divisors = 0
    while i * i < N:
        if N % i == 0:
            divisors += 2
        i += 1
    if i * i == N:
        divisors += 1
    return divisors

assert soluotion(24) == 8