class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

a = Point()
a.set_coords(1,2)
Point.set_coords(Point,1,2)
print(Point.get_coords(Point))
print(Point.__dict__)