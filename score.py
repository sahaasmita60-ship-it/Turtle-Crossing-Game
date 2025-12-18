from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.createlevel()
    def createlevel(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level={self.level}", align="center",font=("Arial",20,"normal"))

    def inclevel(self):
        self.level+=1
        self.createlevel()

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align="center",font=("Arial",50,"normal"))
