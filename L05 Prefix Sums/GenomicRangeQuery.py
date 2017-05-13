# coding=utf-8

"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""
nuc = {'A':1, 'C':2, 'G':3, 'T':4}

def solution(S, P, Q):
    n = len(S)
    prefix_A = [0]*(n+1)
    prefix_C = [0]*(n+1)
    prefix_G = [0]*(n+1)
    prefix_T = [0]*(n+1)

    for i, nucleotid in enumerate(S):
        A = 1 if nucleotid == 'A' else 0
        C = 1 if nucleotid == 'C' else 0
        G = 1 if nucleotid == 'G' else 0
        T = 1 if nucleotid == 'T' else 0
        prefix_A[i+1] = prefix_A[i]+A
        prefix_C[i+1] = prefix_C[i]+C
        prefix_G[i+1] = prefix_G[i]+G
        prefix_T[i+1] = prefix_T[i]+T
    m = len(P)
    R = [0]*m
    for i in range(m):
        start = P[i]
        end = Q[i]
        sum_A = prefix_A[end+1] - prefix_A[start]
        sum_C = prefix_C[end+1] - prefix_C[start]
        sum_G = prefix_G[end+1] - prefix_G[start]
        sum_T = prefix_T[end+1] - prefix_T[start]
        if sum_A > 0:
            R[i] = nuc['A']
        elif sum_C > 0:
            R[i] = nuc['C']
        elif sum_G > 0:
            R[i] = nuc['G']
        elif sum_T > 0:
            R[i] = nuc['T']
    return R

assert solution('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2, 4, 1]

def solution2(S, P, Q):
    n = len(S)
    A = [0] * (n+1)
    C = [0] * (n+1)
    G = [0] * (n+1)
    T = [0] * (n+1)

    for i in xrange(1,n+1):
        if S[i-1] == 'A':
            a,c,g,t = 1,0,0,0
        elif S[i-1] == 'C':
            a,c,g,t = 0,1,0,0
        elif S[i-1] == 'G':
            a,c,g,t = 0,0,1,0
        elif S[i-1] == 'G':
            a,c,g,t = 0,0,0,1
        else:
            a,c,g,t = 0,0,0,0
        A[i] = A[i-1] + a
        C[i] = C[i-1] + c
        G[i] = G[i-1] + g
        T[i] = T[i-1] + t

    ans = [0]*len(P)
    for i in xrange(len(P)):
        start = P[i]
        end = Q[i]

        count_a = A[end+1] - A[start]
        count_c = C[end+1] - C[start]
        count_g = G[end+1] - G[start]
        count_t = T[end+1] - T[start]
        if count_a > 0:
            ans[i] = 1
        elif count_c > 0:
            ans[i] = 2
        elif count_g > 0:
            ans[i] = 3
        else:
            ans[i] = 4
    return ans
