class Point:
    color = 'red'
    circle = 2


# var = Point.__dict__
# print(var)
#
# setattr(Point, 'color', 'circle')
# getattr(Point, 'var', print('False'))
# print(hasattr(Point, 'var'))
# delattr(Point, 'circle')
a, b = Point(), Point()
a.x, a.y = 100, 100
b.x, b.y = 200, 200

