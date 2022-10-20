from shape import Shape

class LShape(Shape):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.squares = [(x,y),(x,y+1),(x,y+2),(x+1,y+2)]