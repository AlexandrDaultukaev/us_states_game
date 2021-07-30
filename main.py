import turtle
import pandas


class State(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.name = ""
        self.penup()

    def set_name(self, name_s, x, y):
        self.goto(x, y)
        self.name = name_s

    def display(self):
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
name_states = data["state"]
for name in name_states:
    # Example: name = Alamaba, data_one_state = state   x   y
    #                                           Alabama 139 -77
    data_one_state = data[data["state"] == name]
    state = State()
    state.set_name(name, int(data_one_state["x"]), int(data_one_state["y"]))
    states.append(state)

game_is_on = True
num_guessed_states = 0
while game_is_on and num_guessed_states != 50:
    answer = sc.textinput(title="Guess the State", prompt=f"What's another state's name?[{num_guessed_states}/50]").title()
    for state in states:
        if answer == state.name:
            state.display()
            states.remove(state)
            num_guessed_states += 1
        elif answer is None:
            game_is_on = False

sc.exitonclick()
