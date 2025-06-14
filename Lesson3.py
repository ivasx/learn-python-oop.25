class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print(self.x, self.y)
        print('Об\'єкт видалено')

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

if __name__ == '__main__':
    point = Point(1, 2)
    print(point.get_coords())