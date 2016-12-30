
class Point:

    def __init__(self, x: double, y: double):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, a: Point, c: Point):
        self.a = a
        self.b = Point(c.x, a.y)
        self.c = c
        self.d = Point(a.x, c.y)
