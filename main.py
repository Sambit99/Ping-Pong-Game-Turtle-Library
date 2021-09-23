from turtle import Screen, speed
from config import SCREEN_HEIGHT,SCREEN_WIDTH
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from border import Border

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle(((SCREEN_WIDTH//2*-1)+50,0))
r_paddle = Paddle(((SCREEN_WIDTH//2)-50,0))
ball = Ball()
scoore = Scoreboard()
border = Border()


screen.listen()
screen.onkey(r_paddle.move_up,'Up')
screen.onkey(r_paddle.move_down,'Down')
screen.onkey(l_paddle.move_up,'w')
screen.onkey(l_paddle.move_down,'s')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detects collison with upper and lower walls
    if ball.ycor() >= (SCREEN_HEIGHT//2)-10 or ball.ycor() < (SCREEN_HEIGHT//2*-1)+20:
        ball.bounce_y()

    # Detects collison with r_paddle
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > (SCREEN_WIDTH//2)-80) or ball.distance(l_paddle) <= 50 and ball.xcor() < (SCREEN_WIDTH//2*-1)+80: 
        # -80/+80 because paddle is 50 pixels far from the wall and paddle is 20 pixel width, 
        # so 50+20+10(10 to ensure that it only touch the surface) is the ideal to detect the collison
        ball.bounce_x()
    
    # r_paddle miss 
    if ball.xcor()>=(SCREEN_WIDTH//2)-30:
        ball.reset_pos()
        scoore.l_point()

    # l_padddle miss
    if ball.xcor()<=(SCREEN_WIDTH//2*-1)+30:
        ball.reset_pos()
        scoore.r_point()
        
    





screen.exitonclick()