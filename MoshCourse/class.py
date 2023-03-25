class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.v = 10
print(point1.v)
point1.draw()
