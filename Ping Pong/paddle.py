from turtle import *

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesie(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    
    def go_up(self):
        new_Y = paddle.ycor() + 15
        paddle.goto(paddle.xcor(), new_Y)
        
    
    def go_down(self):
        new_Y = self.ycor() - 15
        self.goto(paddle.xcor(), new_Y)
