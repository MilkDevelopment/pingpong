from turtle import Turtle, up
from typing import Match
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courrier",40))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courrier",40))
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over!", align="center", font=("Courrier",35))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        