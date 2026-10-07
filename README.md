# 🇺🇸 U.S. States Game

An interactive **U.S. States guessing game** built using **Python, Turtle Graphics, and Pandas**.

The player has to guess all **50 U.S. states**. Every correct answer is displayed on the map at its corresponding coordinates. If the player exits the game before guessing all states, the remaining states are automatically saved to a `states_to_learn.csv` file.

> 📚 **This project was built as part of my Python learning journey to practice Pandas, data processing, Turtle graphics, user input, CSV files, list comprehension, and game logic.**

---

## 📌 Project Overview

The **U.S. States Game** is a geography-based guessing game inspired by the **100 Days of Code: The Complete Python Pro Bootcamp**.

A blank map of the United States is displayed on the screen. The player enters state names through a text input box.

When the player enters a valid state:

```text
Enter State Name
       ↓
Convert to Title Case
       ↓
Check if State Exists
       ↓
Check if Already Guessed
       ↓
Find State Coordinates
       ↓
Write State Name on Map
       ↓
Increase Score
```

If the player clicks **Cancel**, the game finds all states that haven't been guessed and saves them to:

```text
states_to_learn.csv
```

---

## 🎮 Game Features

- 🇺🇸 Interactive U.S. map
- ⌨️ Text-based state input
- 📍 Displays correctly guessed states on the map
- 📊 Tracks the current score
- 🚫 Prevents duplicate guesses
- 🔤 Handles different input capitalization
- 🐼 Uses Pandas to process state data
- 🛑 Handles the Cancel button
- 📄 Generates `states_to_learn.csv`
- 📝 Saves all unguessed states for future learning
- 🧩 Uses Python list comprehension
- 🏁 Ends automatically after all 50 states are guessed

---

## 🕹️ Controls

| Input | Action |
|---|---|
| State name | Submit a guess |
| Cancel | Save remaining states and exit |

Examples:

```text
New York
California
Texas
Florida
```

The program converts the input to title case:

```text
new york → New York

TEXAS → Texas

california → California
```

---

## 🛠️ Technologies Used

- **Python**
- **Turtle Graphics**
- **Pandas**
- **CSV**
- **VS Code**
- **Git & GitHub**

---

## 📂 Project Structure

```text
US-States-Game/

│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── states_to_learn.csv
└── README.md
```

### `main.py`

Contains the complete game logic.

Responsible for:

- Creating the game screen
- Loading the map
- Reading state data
- Getting user input
- Validating guesses
- Preventing duplicate guesses
- Finding coordinates
- Displaying state names
- Tracking the score
- Finding missing states
- Saving missing states

### `50_states.csv`

Contains the original state data:

```text
state
x
y
```

The `x` and `y` values determine where each state name should be displayed on the map.

### `blank_states_img.gif`

The blank U.S. map used as the game background.

### `states_to_learn.csv`

Generated when the player clicks **Cancel** before completing all 50 states.

It contains the states that were not guessed.

Example:

```text
state
Alaska
Arizona
California
Colorado
```

This file can be used later as a personal list of states to learn.

---

# 🧠 How the Game Works

## 1. Load the State Data

Pandas reads the CSV file:

```python
data = pd.read_csv("50_states.csv")
```

The state column is converted into a Python list:

```python
all_states = data["state"].to_list()
```

Conceptually:

```text
data
 ↓
Complete DataFrame

all_states
 ↓
List containing all 50 states
```

---

## 2. Track Guessed States

An empty list stores the states correctly guessed by the player:

```python
guessed_states = []
```

For example:

```text
[]
 ↓
["Texas"]
 ↓
["Texas", "California"]
 ↓
["Texas", "California", "Florida"]
```

The length of this list represents the current score.

---

## 3. Get User Input

The game asks the player for another state:

```python
answer_state = screen.textinput(
    title=f"{len(guessed_states)}/50 States Correct",
    prompt="What's another state's name?"
)
```

The score is displayed in the input window:

```text
15/50 States Correct
```

---

## 4. Handle the Cancel Button

If the player clicks **Cancel**, `textinput()` returns `None`:

```python
if answer_state is None:
```

The program then finds all the states that have not been guessed yet.

---

## 5. Find Missing States Using List Comprehension

Instead of using a traditional `for` loop, the project uses **list comprehension**:

```python
missing_states = [
    state for state in all_states
    if state not in guessed_states
]
```

This checks every state in `all_states` and adds it to `missing_states` only when it has **not** already been guessed.

Conceptually:

```text
all_states
    ↓
Check every state
    ↓
Is state NOT in guessed_states?
    ↓
YES
    ↓
Add to missing_states
```

For example:

```text
All States:
Alabama
Alaska
Arizona
Texas

Guessed:
Alabama
Texas

Missing:
Alaska
Arizona
```

### Why use list comprehension?

List comprehension provides a shorter and cleaner way to create a list based on a condition.

Traditional approach:

```python
missing_states = []

for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)
```

List comprehension:

```python
missing_states = [
    state for state in all_states
    if state not in guessed_states
]
```

Both approaches produce the same result, but list comprehension makes the logic more concise.

---

## 6. Create the Missing States DataFrame

The missing states are converted into a Pandas DataFrame:

```python
missing_data = pd.DataFrame(
    missing_states,
    columns=["state"]
)
```

The result looks like:

```text
       state
0      Alaska
1     Arizona
2  California
```

---

## 7. Save Missing States to CSV

The DataFrame is then saved:

```python
missing_data.to_csv(
    "states_to_learn.csv",
    index=False
)
```

`index=False` prevents Pandas from adding the DataFrame's row numbers to the CSV.

The resulting file contains:

```text
state
Alaska
Arizona
California
```

This file can be used later as a personal list of states to learn.

---

## 8. Normalize the Input

If the player does not click Cancel, the answer is converted to title case:

```python
answer_state = answer_state.title()
```

For example:

```text
new york
    ↓
New York
```

This makes the input easier to compare with the state names in the CSV.

---

## 9. Validate the Guess

The program checks:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

This means:

```text
Is it a valid state?

        AND

Has it not already been guessed?
```

Only when both conditions are true is the answer accepted.

---

## 10. Find the State Coordinates

Once the answer is valid:

```python
state_data = data[data["state"] == answer_state]
```

This filters the DataFrame and returns the row belonging to the guessed state.

The coordinates are then extracted:

```python
state_data["x"].item()
state_data["y"].item()
```

`.item()` extracts the individual coordinate value from the one-row Series.

---

## 11. Display the State

A new Turtle object is created for the state label:

```python
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()
```

It moves to the state's coordinates:

```python
state_turtle.goto(
    state_data["x"].item(),
    state_data["y"].item()
)
```

Then the state name is written:

```python
state_turtle.write(answer_state)
```

---

# 📄 Saving Missing States

One of the important features of this project is saving the states that the player hasn't guessed.

When the player clicks **Cancel**, the program:

```text
Cancel
  ↓
Find unguessed states
  ↓
Create Pandas DataFrame
  ↓
Save as states_to_learn.csv
  ↓
End Game
```

The complete logic is:

```python
if answer_state is None:
    missing_states = [
        state for state in all_states
        if state not in guessed_states
    ]

    missing_data = pd.DataFrame(
        missing_states,
        columns=["state"]
    )

    missing_data.to_csv(
        "states_to_learn.csv",
        index=False
    )

    break
```

This demonstrates how Python and Pandas can work together to process existing data and generate a new CSV file.

---

# 🔄 Complete Game Flow

```text
Start Game

    ↓

Display U.S. Map

    ↓

Load State Data

    ↓

Create State List

    ↓

Create Empty Guessed List

    ↓

Ask for State Name

    ↓

Cancel?
 ┌──YES──→ Find Missing States
 │              ↓
 │        Create DataFrame
 │              ↓
 │        Save CSV
 │              ↓
 │          End Game
 │
 NO
 ↓

Convert to Title Case

    ↓

Valid State?

 ┌──NO──→ Ask Again
 │
 YES
 ↓

Already Guessed?

 ┌──YES──→ Ask Again
 │
 NO
 ↓

Add to Guessed List

    ↓

Find Coordinates

    ↓

Write State Name

    ↓

All 50 Guessed?

 ┌──NO──→ Repeat
 │
 YES
 ↓

End Game
```

---

# 🧩 Key Variables

| Variable | Purpose |
|---|---|
| `screen` | Controls the Turtle window |
| `map_image` | Stores the map image filename |
| `map_turtle` | Displays the background map |
| `data` | Complete Pandas DataFrame |
| `all_states` | List of all 50 states |
| `guessed_states` | States correctly guessed |
| `answer_state` | Current user input |
| `state_data` | Data for the current state |
| `state_turtle` | Writes state names on the map |
| `missing_states` | States not guessed |
| `missing_data` | DataFrame containing missing states |

---

# 🐼 Pandas Concepts Practiced

### Read CSV

```python
data = pd.read_csv("50_states.csv")
```

### Select a Column

```python
data["state"]
```

### Convert Series to List

```python
data["state"].to_list()
```

### Filter a DataFrame

```python
data[data["state"] == answer_state]
```

### Extract a Single Value

```python
state_data["x"].item()
```

### Create a DataFrame

```python
pd.DataFrame(
    missing_states,
    columns=["state"]
)
```

### Write a DataFrame to CSV

```python
missing_data.to_csv(
    "states_to_learn.csv",
    index=False
)
```

---

# 🐍 Python Concepts Practiced

### List

Used to store all states and correctly guessed states:

```python
all_states = data["state"].to_list()

guessed_states = []
```

### List Comprehension

Used to create a list of states that haven't been guessed:

```python
missing_states = [
    state for state in all_states
    if state not in guessed_states
]
```

### Conditional Statements

Used to validate the user's answer:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

### While Loop

Used to continue the game until all 50 states are guessed:

```python
while len(guessed_states) < 50:
```

### String Methods

Used to normalize user input:

```python
answer_state.title()
```

---

# 🐢 Turtle Concepts Practiced

- Creating a Turtle screen
- Setting screen titles
- Adding custom images as Turtle shapes
- Creating multiple Turtle objects
- Moving Turtle objects using coordinates
- Writing text on the screen
- Hiding Turtle objects
- Using `penup()`
- Getting user input with `textinput()`

---

# 🔑 Important Lessons

### `all_states` vs `guessed_states`

```text
all_states
    ↓
All possible answers

guessed_states
    ↓
Answers already guessed
```

---

### `missing_states`

```text
all_states
    -
guessed_states
    ↓
missing_states
```

The list comprehension performs this filtering in a concise way:

```python
missing_states = [
    state for state in all_states
    if state not in guessed_states
]
```

This gives us the states the player still needs to learn.

---

### `data` vs `state_data`

```text
data
 ↓
Complete CSV data

state_data
 ↓
Only the row for the current guessed state
```

---

### `.to_list()` vs `.item()`

Two useful Pandas methods practiced in this project:

```python
data["state"].to_list()
```

converts a Series into a Python list.

While:

```python
state_data["x"].item()
```

extracts a single value from a one-value Series.

---

# 🚀 Future Improvements

Possible improvements:

- 🏆 Add a high-score system
- 💾 Save game progress
- 🔄 Add a restart option
- ⏱️ Add a time limit
- 🔊 Add sound effects
- 🎨 Improve state label styling
- 📊 Display additional statistics
- 📝 Automatically display missed states after the game
- 🗺️ Add maps for other countries

---

# 🎯 Learning Goal

The main goal of this project was to strengthen my understanding of **Python, Pandas, Turtle Graphics, CSV files, list comprehension, and data-driven programming**.

The project combines:

```text
Python
   ↓
Lists & Conditions
   ↓
List Comprehension
   ↓
Pandas
   ↓
CSV Data
   ↓
DataFrame Filtering
   ↓
Turtle Graphics
   ↓
User Input
   ↓
Game Loop
   ↓
CSV Export
   ↓
Interactive Application
```

This project helped me understand how data can be read, processed, displayed, filtered, and eventually exported into a new file.

---

# 📌 Project Status

**Completed** ✅

### Currently Implemented

- U.S. map display
- State data loading
- User input
- Input normalization
- State validation
- Duplicate prevention
- Coordinate lookup
- State name placement
- Score tracking
- Cancel button handling
- Missing-state detection
- List comprehension for missing states
- `states_to_learn.csv` generation
- CSV export without index

---

# 👨‍💻 Author

**Mohammad Mahroof**

Python Developer | Software Developer

---

# 📝 Quick Repository Reminder

When I return to this project later:

```text
main.py
    ↓
Controls the entire game

50_states.csv
    ↓
Contains all state names and coordinates

blank_states_img.gif
    ↓
Provides the U.S. map

states_to_learn.csv
    ↓
Contains states I haven't guessed yet
```

### Core Game Logic

```text
ASK
 ↓
VALIDATE
 ↓
CHECK DUPLICATE
 ↓
FIND COORDINATES
 ↓
WRITE STATE
 ↓
INCREASE SCORE
 ↓
REPEAT
```

### If Player Quits

```text
CANCEL
 ↓
FIND UNGUESSED STATES
 ↓
LIST COMPREHENSION
 ↓
CREATE DATAFRAME
 ↓
SAVE states_to_learn.csv
```

### In One Sentence

> **Guess a valid U.S. state → find its coordinates → write it on the map → increase the score → repeat, and save the remaining states when you quit.**

---

## 📚 Part of My Python Learning Journey

This project is another step in my journey of learning Python through **hands-on projects**.

The main focus was understanding how **Python lists, list comprehension, Pandas data processing, CSV files, Turtle graphics, and game logic** can be combined to build a complete interactive application.