class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = []

for i in range(1, 2001, 2):
    if i == 3:
        obj = Point(i, i, "yellow")
        points.append(obj)
    else:
        obj = Point(i, i)
        points.append(obj)