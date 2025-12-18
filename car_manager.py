import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from score import Score
move_speed=0.1
car=CarManager()
player=Player()
score=Score()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.forward,"Up")
player.createplayer()
game_is_on = True

while game_is_on:
    time.sleep(move_speed)
    screen.update()
    car.createcar()
    car.move()
    
    if player.t.ycor()>290:
       score.inclevel()
       player.reset()
       move_speed*=0.82
    for newcar in car.all:
     if newcar.distance(player.t)<20:
        game_is_on=False
        score.gameover()

screen.exitonclick()
