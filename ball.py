from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
    def move(self):
        
        self.right(45)
        self.goto(self.xcor()+10,self.ycor()+10)