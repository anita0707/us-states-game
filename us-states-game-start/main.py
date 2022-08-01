from turtle import Turtle ,Screen
import pandas as pd

screen = Screen()
turt = Turtle()
screen.title("U.S States Game")

# loading am image in the shape function
image = "blank_states_img.gif"
screen.addshape(image)
turt.shape(image)
count = 0
guess_list = []
game_on = True
# changing guess to title case
while game_on is True:

    guess = screen.textinput(title=f"{count}/50",
                             prompt="What's another state's names?").title()
    
    # creating data frames
    data = pd.read_csv("50_states.csv")
    state_column = data.state.to_list()
    if guess == "Exit":
        game_on = False

    if guess in state_column and guess not in guess_list :
        guess_list.append(guess)
        row_data = (data[data.state == guess])
        new_tut = Turtle()
        new_tut.hideturtle()
        new_tut.penup()
        new_tut.goto(int(row_data.x) , int (row_data.y))
        new_tut.write(guess , font= ("Verdana", 10, "normal"))
        count += 1

# states which have not been guessed by the user

unguessed_data = pd.DataFrame(list (set (state_column)- set (guess_list)))
unguessed_data.to_csv("states_to_learn.csv")


# to get the x and y coordinates of where you check
# def get_mouse_click_coor (x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

