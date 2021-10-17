import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.cars_move()
    screen.update()

    for i in range(0, len(car_manager.all_cars)):
        if player.distance(car_manager.all_cars[i]) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.level += 1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        player.go_start()

screen.exitonclick()