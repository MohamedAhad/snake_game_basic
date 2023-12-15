from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
#
# for position in starting_position:
#     turt = Turtle("square")
#     turt.color("white")
#     turt.penup()
#     turt.goto(position)
#     segments.append(turt)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)
    snake.move()
    # Detection of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()