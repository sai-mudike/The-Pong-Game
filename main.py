from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
score=ScoreBoard()


screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")



is_game_on=True

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_y()

    # collision with paddle
    if ball.xcor()>320 and ball.distance(right_paddle)<50 or ball.xcor()<-320 and ball.distance(left_paddle)<50:
         ball.bounce_x()


    # detect right side miss
    if ball.xcor()> 380:
        ball.reset_position()
        score.l_point()

    # detect left side miss
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()







screen.exitonclick()