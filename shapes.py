class Shape:
    pass

class TShape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.squares = [(x,y),(x+1,y),(x+2,y),(x+1,y+1)]


class ZShape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.squares = [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)]

class LShape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.squares = [(x,y),(x,y+1),(x,y+2),(x+1,y+2)]

class SquareShape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.squares = [(x,y),(x+1,y),(x,y+1),(x+1,y+1)]


