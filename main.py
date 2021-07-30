import turtle
import pandas


class State(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.penup()
        self.hideturtle()

    def set_name(self, name_s, x, y):
        self.goto(x, y)
        self.name = name_s
        #self.write(name, align="center", font=("Arial", 20, "normal"))



sc = turtle.Screen()
sc.title("States Game")
tim = turtle.Turtle()
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

answer = sc.textinput(title="Guess the State", prompt="What's another state's name?")
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

sc.exitonclick()
