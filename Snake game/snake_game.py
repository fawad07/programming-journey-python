from turtle import Screen, Turtle
from snake import *
import time
from food import *
from score import *


#new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
   
snake = Snake()
food = Food()
score = score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)    
    snake.move()
    
    #detect collision from food
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        
        #update score
        score.score_increase()
        
        #detect wall colliion
        if snake.head.xcor > 295 or snake.head.xcor > -295 or snake.head.ycor > 295 or snake.head.ycor > -295:
            game_on = False
       
        #detect collision with tail
        for i in snake.segments[1:]:
            if snake.head.distance(i) < 5:
                game_on = False
                score.game_over()
        
screen.exitonclick()