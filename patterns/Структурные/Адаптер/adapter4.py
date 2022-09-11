from pprint import pprint


class WrongGeometry(Exception):
    pass


class Point:
    def __init__(self, x: float, y: float):
        self.x = float(round(x, 1))
        self.y = float(round(y, 1))

    def __eq__(point1, point2):
        if type(point2) is not Point:
            raise TypeError
        return point1.x == point2.x and point1.y == point2.y

    def __repr__(self):
        return f'({self.x};{self.y})'


# мы должны использовать данную реализацию
def draw_point(point: Point):
    print('.', end='')


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'<Line: ' \
               f'start=({self.start!r}) ' \
               f'end=({self.start!r})>'


class Rectangle:
    def __init__(self, *lines: Line):
        if len(lines) != 4:
            raise WrongGeometry
        for i in range(4):
            if lines[i-1].end != lines[i].start:
                raise WrongGeometry
        self.lines = lines

    def __str__(self):
        res = ''
        for line in self.lines:
            res += str(line) + '\n'
        return res


# система уравнений
# | y1 = k*x1 + b
# | y2 = k*x2 + b
# b = y1 - k*x1
# y2 = k*x2 + y1 - k*x1
# k = (y2 - y1) / (x2 - x1)
# b = y1 - x1*(y2 - y1) / (x2 - x1)

class PointsInLine(list):
    """Адаптер для создания промежуточных точек отрезка, заданного двумя точками начала и конца отрезка."""
    def __init__(self, line: Line, points_scale: float = 1):
        super().__init__(self)
        self.line = line
        self.points_scale = points_scale

        self.append(self.line.start)

        y1, y2 = self.line.start.y, self.line.end.y
        x1, x2 = self.line.start.x, self.line.end.x
        k = (y2 - y1) / (x2 - x1)
        b = y1 - x1 * (y2 - y1) / (x2 - x1)

        for px in range(1, int((x2 - x1)/points_scale)):
            nx = self.line.start.x + px*points_scale
            ny = k*nx + b
            self.append(Point(nx, ny))
        self.append(self.line.end)


l1 = Line(Point(0,0), Point(3,5))
print(l1)
l1_pointed = PointsInLine(l1, 0.1)
pprint(l1_pointed)

print('\t', end='')
for point in l1_pointed:
    draw_point(point)
print()

r1 = Rectangle(
    Line(Point(0,0), Point(5,0)),
    Line(Point(5,0), Point(5,5)),
    Line(Point(5,5), Point(0,5)),
    Line(Point(0,5), Point(0,0)),
)
print(r1)
