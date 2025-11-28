from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.x_move=10
        self.y_move=10


    def move(self):
        
        self.right(45)
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        self.y_move*=-1
