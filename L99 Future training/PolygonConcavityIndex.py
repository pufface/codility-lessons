import math
# score 90%

class Point2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __len__(self):
        return (self.x**2+self.y**2)**0.5

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    __repr__ = __str__

    def angle(self, other):
        dot = self.x * other.x + self.y * other.y
        det = self.x * other.y - self.y * other.x
        return math.atan2(det, dot)


def angle(P1, P2, P3):
    a = Vector(P2.x - P1.x, P2.y - P1.y)
    b = Vector(P3.x - P2.x, P3.y - P2.y)
    angle_rad = math.degrees(a.angle(b))
    return (angle_rad + 360.0) % 360

def is_clockwise(angle_deg):
    return angle_deg > 180

def solution(A):
    n = len(A)
    if n <= 2:
        return -1
    angles = [0] * n
    for i in xrange(2,n):
        angles[i-1] =  angle(A[i-2], A[i-1], A[i])
    angles[-1] = angle(A[-2], A[-1], A[0])
    angles[0] = angle(A[-1], A[0], A[1])
    clockwise = []
    anti_clockwise = []
    for i in xrange(n):
        if is_clockwise(angles[i]):
            clockwise.append(i)
        else:
            anti_clockwise.append(i)
    if not clockwise or not anti_clockwise:
        return -1
    elif len(clockwise) > len(anti_clockwise):
        return anti_clockwise[0]
    else:
        return clockwise[0]

assert solution([Point2D(-1, 3), Point2D(3, 1), Point2D(0, -1), Point2D(-2, 1)] ) == -1
assert solution([Point2D(-1, 3), Point2D(3, 1), Point2D(0, -1), Point2D(-2, 1), Point2D(0,1)] ) == 4
