from turtle import Turtle
from config import SCREEN_HEIGHT,SCREEN_WIDTH
class Paddle(Turtle):
    def __init__(self,pos) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')       
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos)


    # def __init__(self,pos) -> None:
    #     self.paddle = Turtle(shape='square')
    #     

    def move_up(self):
        y_cor = self.ycor()+20
        if y_cor<(SCREEN_HEIGHT//2)-20:
            self.goto(self.xcor(),y_cor)


    def move_down(self):
        y_cor = self.ycor()-20
        if y_cor>(SCREEN_HEIGHT//2*-1)+40:
            self.goto(self.xcor(),y_cor)
