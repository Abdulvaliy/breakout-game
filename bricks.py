from turtle import Turtle


class Bricks(Turtle):
    def __init__(self, position, colour):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.shape('square')
        self.color(colour)
        self.shapesize(1, 3)


