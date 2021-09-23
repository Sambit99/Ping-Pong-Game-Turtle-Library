from turtle import Turtle
from config import SCREEN_HEIGHT,SCREEN_WIDTH

class Border(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,SCREEN_HEIGHT//2)
        self.setheading(270)
        while(self.ycor()>=(SCREEN_HEIGHT//2*-1)):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        # self.penup()
