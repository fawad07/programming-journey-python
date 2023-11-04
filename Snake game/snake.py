from turtle import Screen, Turtle
import time

STARTING_POS = [(0,0), (-25,0), (-50, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)
    
             
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
   
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    
    
    
    def move(self):
        #MOVE snake
        for i in range(len(self.segments)-1, 0, -1):
            newX = self.segments[i-1].xcor()
            newY = self.segments[i-1].ycor()
            self.segments[i].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
