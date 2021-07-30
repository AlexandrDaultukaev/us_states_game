import turtle
import pandas


class State(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.penup()
        self.hideturtle()

    def set_name(self, name, x, y):
        self.goto(x, y)
        self.name = name
        self.write(name, align="center", font=("Arial", 20, "normal"))


sc = turtle.Screen()
sc.title("States Game")
tim = turtle.Turtle()
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

answer = sc.textinput(title="Guess the State", prompt="What's another state's name?")

data = pandas.read_csv("50_states.csv")

sc.exitonclick()
