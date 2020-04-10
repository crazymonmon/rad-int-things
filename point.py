class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "x: %d y: %d" % (self.x, self.y)
