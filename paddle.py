from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('steelblue')
        self.shapesize(1, 6)
        self.penup()
        self.setposition(position)

    def go_right(self):
        new_right = self.xcor() + 50
        self.goto(new_right, self.ycor())

    def go_left(self):
        new_left = self.xcor() - 50
        self.goto(new_left, self.ycor())

    def go_up(self):
        new_up = self.ycor() + 20
        self.goto(self.xcor(), new_up)

    def go_down(self):
        new_down = self.ycor() - 20
        self.goto(self.xcor(), new_down)

