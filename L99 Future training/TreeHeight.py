class Tree(object):
    x = 0
    l = None
    r = None

    def __init__(self, tree):
        assert tree is not None
        self.x = tree[0]
        self.l = Tree(tree[1]) if tree[1] is not None else None
        self.r = Tree(tree[2]) if tree[2] is not None else None

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.l, self.r)

def solution(T):
    print T
    if T is None:
        return -1
    else:
        return 1 + max(solution(T.l), solution(T.r))

assert solution(Tree((5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None)))) == 2
assert solution(None) == -1
assert solution(Tree((3,None,None))) == 0