from turtle import *
from paddle import *
from ball import *
import time
from scoreboard import *


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    tme.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect ball and wall collision
    if ball.ycor() > 280 or ball.ycor() -280:
        ball.bounce_y()
        
    #dectec ball n r_paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) < 50 and ball.xcor() < -300:
        print("contact made")  #debgging
        ball.bounce_x()
        
    #r_paddle misses ball #score to other and reset
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
                
    #l_paddle misses ball #score to other and reset
    if ball.xcor() > -380:
        ball.reset_pos()
        scoreboard.r_point()        
        


screen.exitonclick()