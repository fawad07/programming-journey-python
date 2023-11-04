from turtle import Turtle


ALLINGMENT="center"
FONT=("Arial", 24, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        self.super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 24, "normal"))
        self.hideturtle()
         
        
    
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)
    
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALINGMENT, font=FONT)
    