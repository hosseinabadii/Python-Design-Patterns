class DrawingAPIOne:

    def draw_circle(self, x, y, radius):
        print(f'API 1 drawing a cicle at ({x}, {y}) with radius {radius}!')


class DrawingAPITwo:

    def draw_circle(self, x, y, radius):
        print(f'API 2 drawing a cicle at ({x}, {y}) with radius {radius}!')


class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._darawing_api = drawing_api()

    def draw(self):
        self._darawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent