import turtle
import pandas


class State(turtle.Turtle):
    def __init__(self, name_s, x, y):
        super().__init__()
        self.hideturtle()
        self.name = name_s
        self.penup()
        self.goto(x, y)
        self.write(self.name, align="center", font=("Arial", 10, "normal"))


sc = turtle.Screen()
sc.title("States Game")
tim = turtle.Turtle()
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

states = []
# read data from csv
data = pandas.read_csv("50_states.csv")
name_states = data["state"].to_list()

game_is_on = True
num_guessed_states = 0
while game_is_on and num_guessed_states != 50:
    answer = sc.textinput(title="Guess the State", prompt=f"What's another state's name?[{num_guessed_states}/50]").title()
    for state in name_states:
        if answer == state:
            t = State(state, int(data[data.state == state]["x"]), int(data[data.state == state]["y"]))
            name_states.remove(state)
            num_guessed_states += 1
        elif answer is None:
            game_is_on = False

sc.exitonclick()
