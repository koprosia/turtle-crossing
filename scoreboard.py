from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x=-250, y=260)
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", "False", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", "False", font=FONT)