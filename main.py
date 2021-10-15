from turtle import Screen, Turtle, exitonclick, goto, xcor
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

gameState = True

while gameState:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Wall collision
    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce_y()

    #r_Paddle collision
    if ball.distance(r_paddle) < 50  and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #loss right detection 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #loss left detection 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
