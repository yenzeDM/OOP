class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        lines = [self.a, self.b, self.c]
        tp = [int, float]
        for i in lines:
            if type(i) not in tp or i <= 0:
                return 1
        if (a + b) > c or (b + c) > a or (c + a) > b:
            return 3
        else:
            return 2


a, b, c = map(int, map(float, input().split()))

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())