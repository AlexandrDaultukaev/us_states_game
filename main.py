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
# read data from CSV
data = pandas.read_csv("50_states.csv")
name_states = data["state"].to_list()

game_is_on = True
num_guessed_states = 0
while game_is_on and num_guessed_states != 50:
    answer = sc.textinput(title="Guess the State", prompt=f"What's another state's name?[{num_guessed_states}/50]")
    for state in name_states:
        if answer is None:
            game_is_on = False
        elif answer.title() == state:
            x = int(data[data.state == state]["x"])
            y = int(data[data.state == state]["y"])
            t = State(state, x, y)
            name_states.remove(state)
            num_guessed_states += 1

# print missing states to CSV
if num_guessed_states != 50:
    missing_states = pandas.DataFrame(name_states)
    missing_states.to_csv("missing_states.csv")

sc.exitonclick()
