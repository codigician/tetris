from shape import Shape

class TShape(Shape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.squares = [(x,y),(x+1,y),(x+2,y),(x+1,y+1)]