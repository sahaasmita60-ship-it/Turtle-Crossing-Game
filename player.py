from turtle import Turtle
class Player():

   def createplayer(self):
      self.t=Turtle()
      self.t.left(90)
      self.t.penup()
      self.t.goto(0,-280)
      self.t.shape("turtle")
      self.t.color("black")
      self.x=self.t.xcor()
   def forward(self):
      self.t.forward(10)

   def reset(self):
      self.t.goto(0,-280)

   def createagain(self):
      self.t.clear()
      self.t.goto(0,-280)
