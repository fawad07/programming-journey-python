from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")

        
        
    def refresh(self):
        rndX = random.randint(-280, 280)
        rndY = random.randint(-280, 280)
        self.goto(rndX,rndY)
        