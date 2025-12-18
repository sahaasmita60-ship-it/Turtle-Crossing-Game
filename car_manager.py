from turtle import Turtle
from player import Player
player=Player()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_distance = 5
move_increment = 10
import random
game_is_on=True

class CarManager:

    def __init__(self):
      self.all=[]

      
    def createcar(self):
    
     self.chance=random.randint(1,6)
     if self.chance==1:
        self.t=Turtle()
        self.t.penup()
        self.t.shape("square")
        self.t.shapesize(1,3)
        self.t.color(random.choice(colors))
        self.num=random.randint(-250,250)
        self.t.goto(300,self.num)
        self.all.append(self.t)
        
    def move(self):
        for self.t in self.all:
         self.t.backward(10)
    

