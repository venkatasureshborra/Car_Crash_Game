from turtle import Turtle
FONT= ("Courier", 24 , "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-300,265)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"LEVEL:{self.level}" ,align="Left",font=FONT)
    def level_up(self):
        self.level+=1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
