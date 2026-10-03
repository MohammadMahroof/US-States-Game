import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)
map_turtle.penup()

# -------------------- Load State Data --------------------
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

# -------------------- Game Loop --------------------
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", 
        prompt="What's another state's name?"
    )

    # Stop the game if the user clicks Cancel.
    if answer_state is None:
        break

    answer_state = answer_state.title()

    # Check that the answer is a valid state 
    # and has not already been guessed.
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()

        # Move to the state's coordinates.
        state_turtle.goto(state_data["x"].item(), state_data["y"].item())

        # Write the state name on the map.
        state_turtle.write(answer_state)

        
# -------------------- End Game --------------------

screen.exitonclick()