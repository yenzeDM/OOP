from random import randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
classes = [Line, Rect, Ellipse]
for _ in range(0, 217):
    choose_class = randint(0, 2)
    random_number = [randint(0, 1500) for _ in range(0, 4)]
    elements.append(classes[choose_class](*random_number))

for i in elements:
    if type(i) == Line:
        i.sp = (0, 0)
        i.ep = (0, 0)