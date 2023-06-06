from turtle import Turtle
import random
COLORS=["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE
        
    def create_car(self):
        ch=random.randrange(1, 6)
        if ch==1:
            t=Turtle("square")
            t.penup()
            t.shapesize(stretch_wid=1 , stretch_len=2)
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.goto(300, random.randint(-250,250))
            self.cars.append(t)

    def car_move(self):
        for car in self.cars:
            car.fd(self.car_speed)

    def speed_up(self):
         self.car_speed+= MOVE_INCREMENT











