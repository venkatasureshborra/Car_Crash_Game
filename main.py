from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Score
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)

player = Player()
car = CarManager()
score=Score()
sc.listen()
sc.onkey(player.go_up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    sc.update()
    car.create_car()
    car.car_move()

    for car_dist  in car.cars:
        if car_dist.distance(player) < 20:
            game_on =False
            score.game_over()


    if player.ycor()> 280:
        player.restart()
        car.speed_up()
        score.level_up()


sc.exitonclick()