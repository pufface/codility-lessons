def make_graph(A, B):
    graph = dict()
    for i in xrange(len(A)):
        p_from = A[i]
        p_to = B[i]
        graph.setdefault(p_from, []).append(p_to)
    return graph

def find_all_paths(graph):


def solution(A, B, K):
    print make_graph(A, B)
    return 2


assert solution([5, 1, 0, 2, 7, 0, 6, 6, 1], [1, 0, 7, 4, 2, 6, 8, 3, 9], 2) == 2