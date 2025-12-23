from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        with open("score.txt") as board:
            self.highlevel=int(board.read())
        self.createlevel()
    def createlevel(self):
        self.clear()
        self.goto(-130,250)
        self.write(f"Level={self.level}, Highest Level={self.highlevel}", align="center",font=("Arial",20,"normal"))

    def inclevel(self):
        self.level+=1
        self.createlevel()


    def reset(self):
        if self.level>self.highlevel:
            self.highlevel=self.level
            with open("score.txt") as scoretext:
                file=scoretext.read()
                content=int(file)
                if content<self.highlevel:
                    with open("score.txt","w") as write:
                        self.highestscore=str(self.highlevel)
                        write.write(self.highestscore)

        self.score=0
        self.createlevel()
        
