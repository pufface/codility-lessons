'''
Consider n coins aligned in a row. Each coin is showing heads at the beginning.
1 2 3 4 5 6 7 8 9 10
H H H H H H H H H H
Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
that are multiples of i. That is, person i flips coins i, 2i, 3i ... until no more appropriate
coins remain. The goal is to count the number of coins showing tails. In the above example,
the final configuration is:
1 2 3 4 5 6 7 8 9 10
T H H T H H H H T H

i = 1 => 1,2,3,4,5,6,7,8,9,10
i = 2 => 2,4,6,8,10
i = 3 => 3,6,9
i = 4 => 4,8
i = 5 => 5,10
i = 6 => 6
i = 7 => 7
i = 8 => 8
i = 9 => 9
i = 10 => 10

'''

# O(n log n)
def coins(n):
    coin = ['H']*n
    for i in xrange(1,n+1):
        for k in xrange(i, n+1, i):
            coin[k-1] = 'H' if coin[k-1] == 'T' else 'T'
    return coin

assert coins(10) == ['T', 'H', 'H', 'T', 'H', 'H', 'H', 'H', 'T', 'H']