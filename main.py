from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

COLORS = ["maroon", "red", "coral", "royalblue", "steelblue", "blue", "olive", "green", "lime"]
all_bricks = []
broken = 0

scoreboard = Scoreboard()
my_paddle = Paddle((0, -270))
ball = Ball()

screen = Screen()
screen.bgcolor('white')
screen.setup(800, 600)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

screen.onkey(my_paddle.go_right, 'Right')
screen.onkey(my_paddle.go_left, 'Left')
screen.onkey(my_paddle.go_right, 'd')
screen.onkey(my_paddle.go_left, 'a')
screen.onkey(my_paddle.go_up, 'Up')
screen.onkey(my_paddle.go_down, 'Down')
screen.onkey(my_paddle.go_up, 'w')
screen.onkey(my_paddle.go_down, 's')


for n in range(0, 716, 65):
    bricks1 = Bricks((-360 + n, 280 - 50), COLORS[0])
    bricks3 = Bricks((-360 + n, 230 - 50), COLORS[2])
    bricks5 = Bricks((-360 + n, 180 - 50), COLORS[4])
    bricks7 = Bricks((-360 + n, 130 - 50), COLORS[6])
    bricks9 = Bricks((-360 + n, 80 - 50), COLORS[8])
    all_bricks.append(bricks1)
    all_bricks.append(bricks3)
    all_bricks.append(bricks5)
    all_bricks.append(bricks7)
    all_bricks.append(bricks9)


for n in range(0, 700, 65):
    bricks2 = Bricks((-330 + n, 255 - 50), COLORS[1])
    bricks4 = Bricks((-330 + n, 205 - 50), COLORS[3])
    bricks6 = Bricks((-330 + n, 155 - 50), COLORS[5])
    bricks8 = Bricks((-330 + n, 105 - 50), COLORS[7])
    all_bricks.append(bricks2)
    all_bricks.append(bricks4)
    all_bricks.append(bricks6)
    all_bricks.append(bricks8)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(my_paddle) < 78 and ball.ycor() < my_paddle.ycor() + 30:
        ball.speed(2)
        ball.bounce_y()

    for brick in all_bricks:
        if brick.distance(ball) < 40:
            ball.bounce_x()
            ball.bounce_y()
            brick.goto(2000, 3000)
            broken += 1
        if broken == 104:
            ball.reset_position()
            scoreboard.point()

#   if you miss a ball
    if ball.ycor() < -280:
        scoreboard.life()
        ball.reset_position()
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
