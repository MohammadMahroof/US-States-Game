# 🇺🇸 U.S. States Game

An interactive **U.S. States guessing game** built using **Python, Turtle Graphics, and Pandas**.

The player has to guess all **50 U.S. states**. Every correct answer is displayed on the map at its corresponding coordinates. The game keeps track of the number of correctly guessed states and prevents duplicate guesses.

> 📚 **This project was built as part of my Python learning journey to practice Pandas, data processing, Turtle graphics, user input, and game logic.**

---

## 📌 Project Overview

The **U.S. States Game** is a simple geography-based game inspired by the U.S. States project from the **100 Days of Code: The Complete Python Pro Bootcamp**.

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

The game continues until all 50 states are guessed or the player clicks **Cancel**.

---

## 🎮 Game Features

* 🇺🇸 Interactive U.S. map
* ⌨️ Text-based state input
* 📍 Displays guessed states at their correct coordinates
* 📊 Tracks the current score
* 🚫 Prevents duplicate guesses
* 🔤 Handles different input capitalization
* 🐼 Uses Pandas to process state data
* 🛑 Handles the Cancel button
* 🏁 Ends automatically after all 50 states are guessed
* 🧩 Uses separate Turtle objects for the map and state labels

---

## 🕹️ Controls

The game uses a text input box rather than keyboard movement.

| Input      | Action         |
| ---------- | -------------- |
| State name | Submit a guess |
| Cancel     | Stop the game  |

Examples:

```text
New York
California
Texas
Florida
```

The program also converts input into title case:

```text
new york → New York
CALIFORNIA → California
texas → Texas
```

---

## 🛠️ Technologies Used

* **Python**
* **Turtle Graphics**
* **Pandas**
* **CSV**
* **VS Code**
* **Git & GitHub**

---

## 📂 Project Structure

```text
US-States-Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── README.md
```

### `main.py`

Contains the complete game logic.

It is responsible for:

* Creating the game screen
* Loading the map
* Reading the CSV file
* Creating the list of states
* Getting user input
* Validating guesses
* Preventing duplicate guesses
* Finding state coordinates
* Displaying state names
* Tracking the score
* Ending the game

**In simple terms:** `main.py` controls the entire game.

---

### `50_states.csv`

Contains the data required to place each state on the map.

The important columns are:

```text
state
x
y
```

Example:

```text
state        x       y
Alabama     139    -163
Alaska     -224     172
Arizona    -224     -... 
```

The `x` and `y` values represent the position where the state name should be written on the map.

---

### `blank_states_img.gif`

This is the blank U.S. map used as the background of the game.

The map provides the visual reference while the program dynamically writes the correctly guessed state names.

---

# 🧠 How the Game Works

## 1. Create the Game Screen

The Turtle screen is created and given a title.

```python
screen = turtle.Screen()
screen.title("U.S. States Game")
```

The map image is then registered as a Turtle shape.

```python
image = "blank_states_img.gif"
screen.addshape(image)
```

A separate Turtle object displays the map:

```python
map_turtle = turtle.Turtle()
map_turtle.shape(image)
map_turtle.penup()
```

The `map_turtle` is used only for the background map.

---

## 2. Load the State Data

Pandas reads the CSV file:

```python
data = pd.read_csv("50_states.csv")
```

`data` is a Pandas **DataFrame** containing all state information.

The state column is converted into a normal Python list:

```python
all_states = data.state.to_list()
```

Now:

```text
data
 ↓
Complete state DataFrame

all_states
 ↓
List containing all 50 state names
```

---

## 3. Store Guessed States

An empty list is created to keep track of correct answers:

```python
guessed_states = []
```

Whenever the player correctly guesses a new state, it is added to this list.

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

The length of this list represents the player's score.

---

## 4. Start the Game Loop

The game continues until all 50 states have been guessed:

```python
while len(guessed_states) < 50:
```

This means:

```text
0 states  → Continue
10 states → Continue
25 states → Continue
49 states → Continue
50 states → Stop
```

---

## 5. Get User Input

The player enters a state name using Turtle's `textinput()`:

```python
answer_state = screen.textinput(
    title=f"{len(guessed_states)}/50 States Correct",
    prompt="What's another state's name?"
)
```

The title also displays the current score.

For example:

```text
15/50 States Correct
```

---

## 6. Handle the Cancel Button

When the player clicks **Cancel**, `textinput()` returns `None`.

The program checks for this:

```python
if answer_state is None:
    break
```

This safely exits the game loop.

Without this check, the program could attempt to perform string operations on `None`.

---

## 7. Convert Input to Title Case

The player's answer is converted to title case:

```python
answer_state = answer_state.title()
```

This allows different capitalization styles to be handled consistently.

For example:

```text
new york
    ↓
New York

TEXAS
    ↓
Texas

california
    ↓
California
```

`.title()` is especially useful for state names containing multiple words.

---

## 8. Validate the Guess

The program checks two conditions:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

This means:

```text
Is it a valid state?
        AND
Has it not already been guessed?
```

Both conditions must be true.

### Valid New Guess

```text
"Texas"
   ↓
Exists in all_states?
   ↓
YES
   ↓
Already guessed?
   ↓
NO
   ↓
Accept the answer
```

### Duplicate Guess

```text
"Texas"
   ↓
Exists in all_states?
   ↓
YES
   ↓
Already guessed?
   ↓
YES
   ↓
Ignore the answer
```

---

## 9. Add the Correct Guess

When a valid new state is entered:

```python
guessed_states.append(answer_state)
```

The state is added to the list of correctly guessed states.

This also increases the score because:

```python
len(guessed_states)
```

now becomes one number higher.

---

## 10. Find the State's Coordinates

The program filters the DataFrame to find the row belonging to the guessed state:

```python
state_data = data[data["state"] == answer_state]
```

This is an important Pandas operation.

The expression:

```python
data["state"] == answer_state
```

creates a Boolean condition for every row.

For example:

```text
Alabama     → False
Alaska      → False
Arizona     → False
Texas       → True
Utah        → False
```

Pandas then uses this condition to return only the matching row.

---

## 11. Extract the Coordinates

The x and y coordinates are retrieved using:

```python
state_data["x"].item()
state_data["y"].item()
```

`.item()` extracts the single value from the one-row Series.

Conceptually:

```text
DataFrame
   ↓
Matching state row
   ↓
x column / y column
   ↓
.item()
   ↓
Single coordinate value
```

This gives Turtle the individual numbers needed by:

```python
turtle.goto(x, y)
```

---

## 12. Create a Turtle for the State Name

A new Turtle object is created for every correct state:

```python
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()
```

The Turtle is hidden because we only need it to write the state name.

`penup()` prevents it from drawing a line while moving.

---

## 13. Move to the State's Position

The Turtle moves to the coordinates stored in the CSV:

```python
state_turtle.goto(
    state_data["x"].item(),
    state_data["y"].item()
)
```

The coordinates determine exactly where the state name appears on the map.

---

## 14. Write the State Name

Finally, the state name is displayed:

```python
state_turtle.write(answer_state)
```

For example:

```text
Player enters:
Texas

        ↓

Find Texas coordinates

        ↓

Move Turtle to coordinates

        ↓

Write "Texas" on the map
```

---

# 🐼 Pandas Concepts Practiced

This project helped me practice several important Pandas concepts.

### Reading a CSV

```python
data = pd.read_csv("50_states.csv")
```

Reads the CSV file into a DataFrame.

### Selecting a Column

```python
data["state"]
```

Returns the `state` column as a Pandas Series.

### Converting a Column to a List

```python
data["state"].to_list()
```

Converts the state column into a normal Python list.

### Filtering a DataFrame

```python
data[data["state"] == answer_state]
```

Returns only the row matching the user's answer.

### Extracting a Single Value

```python
state_data["x"].item()
```

Extracts one coordinate value from the filtered data.

---

# 🐢 Turtle Concepts Practiced

This project also helped me understand:

* Creating a Turtle screen
* Setting screen titles
* Registering custom images as Turtle shapes
* Creating multiple Turtle objects
* Moving Turtle objects using coordinates
* Writing text on the screen
* Hiding Turtle objects
* Using `penup()`
* Getting user input with `textinput()`
* Keeping a background object separate from writing objects

---

# 🔄 Main Game Loop

The complete game logic can be summarized as:

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
 ┌──YES──→ End Game
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
Find State Coordinates
    ↓
Create Turtle
    ↓
Move to Coordinates
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

Understanding these variables makes it much easier to understand the whole project later.

| Variable         | Purpose                                  |
| ---------------- | ---------------------------------------- |
| `screen`         | Controls the Turtle game window          |
| `image`          | Stores the map image filename            |
| `map_turtle`     | Displays the background map              |
| `data`           | Pandas DataFrame containing state data   |
| `all_states`     | List containing all 50 state names       |
| `guessed_states` | List containing correctly guessed states |
| `answer_state`   | Current user input                       |
| `state_data`     | DataFrame row for the guessed state      |
| `state_turtle`   | Turtle used to write the state name      |

---

# 🔑 Most Important Logic

The most important condition in the project is:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

It combines two checks:

```text
Valid State
     +
Not Already Guessed
     ↓
Accept Guess
```

This simple condition prevents invalid and duplicate answers from being added to the score.

---

# 🧠 Important Lessons

### `.title()` vs `.capitalize()`

`.title()` is useful because state names can contain multiple words.

```python
"new york".title()
```

produces:

```text
New York
```

Whereas `.capitalize()` would produce:

```text
New york
```

---

### `data` vs `all_states`

They contain different types of information:

```text
data
 ↓
Complete DataFrame
 ↓
state + x + y
```

while:

```text
all_states
 ↓
["Alabama", "Alaska", ..., "Wyoming"]
```

`all_states` is used for validation, while `data` is used to find coordinates.

---

### Why `guessed_states` is a Separate List

`all_states` contains every possible answer.

`guessed_states` contains only the answers the player has already correctly entered.

```text
all_states
    ↓
Possible answers

guessed_states
    ↓
Already answered
```

This allows the program to prevent duplicate guesses.

---

# 🏗️ Program Structure

Although this project uses one main Python file, the logic can still be understood as separate responsibilities:

```text
                 U.S. States Game
                        │
        ┌───────────────┼───────────────┐
        │               │               │
      Turtle          Pandas        Game Logic
        │               │               │
      Map           CSV Data        Validation
      Input          States         Score
      Writing        Coordinates     Game Loop
```

Each technology has a clear role:

```text
Turtle
  ↓
Displays and interacts with the game

Pandas
  ↓
Reads and searches state data

Python
  ↓
Controls the game logic
```

---

# ▶️ How to Run

### 1. Clone the Repository

```bash
git clone # 🇺🇸 U.S. States Game

An interactive **U.S. States guessing game** built using **Python, Turtle Graphics, and Pandas**.

The player has to guess all **50 U.S. states**. Every correct answer is displayed on the map at its corresponding coordinates. The game keeps track of the number of correctly guessed states and prevents duplicate guesses.

> 📚 **This project was built as part of my Python learning journey to practice Pandas, data processing, Turtle graphics, user input, and game logic.**

---

## 📌 Project Overview

The **U.S. States Game** is a simple geography-based game inspired by the U.S. States project from the **100 Days of Code: The Complete Python Pro Bootcamp**.

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

The game continues until all 50 states are guessed or the player clicks **Cancel**.

---

## 🎮 Game Features

* 🇺🇸 Interactive U.S. map
* ⌨️ Text-based state input
* 📍 Displays guessed states at their correct coordinates
* 📊 Tracks the current score
* 🚫 Prevents duplicate guesses
* 🔤 Handles different input capitalization
* 🐼 Uses Pandas to process state data
* 🛑 Handles the Cancel button
* 🏁 Ends automatically after all 50 states are guessed
* 🧩 Uses separate Turtle objects for the map and state labels

---

## 🕹️ Controls

The game uses a text input box rather than keyboard movement.

| Input      | Action         |
| ---------- | -------------- |
| State name | Submit a guess |
| Cancel     | Stop the game  |

Examples:

```text
New York
California
Texas
Florida
```

The program also converts input into title case:

```text
new york → New York
CALIFORNIA → California
texas → Texas
```

---

## 🛠️ Technologies Used

* **Python**
* **Turtle Graphics**
* **Pandas**
* **CSV**
* **VS Code**
* **Git & GitHub**

---

## 📂 Project Structure

```text
US-States-Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── README.md
```

### `main.py`

Contains the complete game logic.

It is responsible for:

* Creating the game screen
* Loading the map
* Reading the CSV file
* Creating the list of states
* Getting user input
* Validating guesses
* Preventing duplicate guesses
* Finding state coordinates
* Displaying state names
* Tracking the score
* Ending the game

**In simple terms:** `main.py` controls the entire game.

---

### `50_states.csv`

Contains the data required to place each state on the map.

The important columns are:

```text
state
x
y
```

Example:

```text
state        x       y
Alabama     139    -163
Alaska     -224     172
Arizona    -224     -... 
```

The `x` and `y` values represent the position where the state name should be written on the map.

---

### `blank_states_img.gif`

This is the blank U.S. map used as the background of the game.

The map provides the visual reference while the program dynamically writes the correctly guessed state names.

---

# 🧠 How the Game Works

## 1. Create the Game Screen

The Turtle screen is created and given a title.

```python
screen = turtle.Screen()
screen.title("U.S. States Game")
```

The map image is then registered as a Turtle shape.

```python
image = "blank_states_img.gif"
screen.addshape(image)
```

A separate Turtle object displays the map:

```python
map_turtle = turtle.Turtle()
map_turtle.shape(image)
map_turtle.penup()
```

The `map_turtle` is used only for the background map.

---

## 2. Load the State Data

Pandas reads the CSV file:

```python
data = pd.read_csv("50_states.csv")
```

`data` is a Pandas **DataFrame** containing all state information.

The state column is converted into a normal Python list:

```python
all_states = data.state.to_list()
```

Now:

```text
data
 ↓
Complete state DataFrame

all_states
 ↓
List containing all 50 state names
```

---

## 3. Store Guessed States

An empty list is created to keep track of correct answers:

```python
guessed_states = []
```

Whenever the player correctly guesses a new state, it is added to this list.

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

The length of this list represents the player's score.

---

## 4. Start the Game Loop

The game continues until all 50 states have been guessed:

```python
while len(guessed_states) < 50:
```

This means:

```text
0 states  → Continue
10 states → Continue
25 states → Continue
49 states → Continue
50 states → Stop
```

---

## 5. Get User Input

The player enters a state name using Turtle's `textinput()`:

```python
answer_state = screen.textinput(
    title=f"{len(guessed_states)}/50 States Correct",
    prompt="What's another state's name?"
)
```

The title also displays the current score.

For example:

```text
15/50 States Correct
```

---

## 6. Handle the Cancel Button

When the player clicks **Cancel**, `textinput()` returns `None`.

The program checks for this:

```python
if answer_state is None:
    break
```

This safely exits the game loop.

Without this check, the program could attempt to perform string operations on `None`.

---

## 7. Convert Input to Title Case

The player's answer is converted to title case:

```python
answer_state = answer_state.title()
```

This allows different capitalization styles to be handled consistently.

For example:

```text
new york
    ↓
New York

TEXAS
    ↓
Texas

california
    ↓
California
```

`.title()` is especially useful for state names containing multiple words.

---

## 8. Validate the Guess

The program checks two conditions:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

This means:

```text
Is it a valid state?
        AND
Has it not already been guessed?
```

Both conditions must be true.

### Valid New Guess

```text
"Texas"
   ↓
Exists in all_states?
   ↓
YES
   ↓
Already guessed?
   ↓
NO
   ↓
Accept the answer
```

### Duplicate Guess

```text
"Texas"
   ↓
Exists in all_states?
   ↓
YES
   ↓
Already guessed?
   ↓
YES
   ↓
Ignore the answer
```

---

## 9. Add the Correct Guess

When a valid new state is entered:

```python
guessed_states.append(answer_state)
```

The state is added to the list of correctly guessed states.

This also increases the score because:

```python
len(guessed_states)
```

now becomes one number higher.

---

## 10. Find the State's Coordinates

The program filters the DataFrame to find the row belonging to the guessed state:

```python
state_data = data[data["state"] == answer_state]
```

This is an important Pandas operation.

The expression:

```python
data["state"] == answer_state
```

creates a Boolean condition for every row.

For example:

```text
Alabama     → False
Alaska      → False
Arizona     → False
Texas       → True
Utah        → False
```

Pandas then uses this condition to return only the matching row.

---

## 11. Extract the Coordinates

The x and y coordinates are retrieved using:

```python
state_data["x"].item()
state_data["y"].item()
```

`.item()` extracts the single value from the one-row Series.

Conceptually:

```text
DataFrame
   ↓
Matching state row
   ↓
x column / y column
   ↓
.item()
   ↓
Single coordinate value
```

This gives Turtle the individual numbers needed by:

```python
turtle.goto(x, y)
```

---

## 12. Create a Turtle for the State Name

A new Turtle object is created for every correct state:

```python
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()
```

The Turtle is hidden because we only need it to write the state name.

`penup()` prevents it from drawing a line while moving.

---

## 13. Move to the State's Position

The Turtle moves to the coordinates stored in the CSV:

```python
state_turtle.goto(
    state_data["x"].item(),
    state_data["y"].item()
)
```

The coordinates determine exactly where the state name appears on the map.

---

## 14. Write the State Name

Finally, the state name is displayed:

```python
state_turtle.write(answer_state)
```

For example:

```text
Player enters:
Texas

        ↓

Find Texas coordinates

        ↓

Move Turtle to coordinates

        ↓

Write "Texas" on the map
```

---

# 🐼 Pandas Concepts Practiced

This project helped me practice several important Pandas concepts.

### Reading a CSV

```python
data = pd.read_csv("50_states.csv")
```

Reads the CSV file into a DataFrame.

### Selecting a Column

```python
data["state"]
```

Returns the `state` column as a Pandas Series.

### Converting a Column to a List

```python
data["state"].to_list()
```

Converts the state column into a normal Python list.

### Filtering a DataFrame

```python
data[data["state"] == answer_state]
```

Returns only the row matching the user's answer.

### Extracting a Single Value

```python
state_data["x"].item()
```

Extracts one coordinate value from the filtered data.

---

# 🐢 Turtle Concepts Practiced

This project also helped me understand:

* Creating a Turtle screen
* Setting screen titles
* Registering custom images as Turtle shapes
* Creating multiple Turtle objects
* Moving Turtle objects using coordinates
* Writing text on the screen
* Hiding Turtle objects
* Using `penup()`
* Getting user input with `textinput()`
* Keeping a background object separate from writing objects

---

# 🔄 Main Game Loop

The complete game logic can be summarized as:

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
 ┌──YES──→ End Game
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
Find State Coordinates
    ↓
Create Turtle
    ↓
Move to Coordinates
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

Understanding these variables makes it much easier to understand the whole project later.

| Variable         | Purpose                                  |
| ---------------- | ---------------------------------------- |
| `screen`         | Controls the Turtle game window          |
| `image`          | Stores the map image filename            |
| `map_turtle`     | Displays the background map              |
| `data`           | Pandas DataFrame containing state data   |
| `all_states`     | List containing all 50 state names       |
| `guessed_states` | List containing correctly guessed states |
| `answer_state`   | Current user input                       |
| `state_data`     | DataFrame row for the guessed state      |
| `state_turtle`   | Turtle used to write the state name      |

---

# 🔑 Most Important Logic

The most important condition in the project is:

```python
if answer_state in all_states and answer_state not in guessed_states:
```

It combines two checks:

```text
Valid State
     +
Not Already Guessed
     ↓
Accept Guess
```

This simple condition prevents invalid and duplicate answers from being added to the score.

---

# 🧠 Important Lessons

### `.title()` vs `.capitalize()`

`.title()` is useful because state names can contain multiple words.

```python
"new york".title()
```

produces:

```text
New York
```

Whereas `.capitalize()` would produce:

```text
New york
```

---

### `data` vs `all_states`

They contain different types of information:

```text
data
 ↓
Complete DataFrame
 ↓
state + x + y
```

while:

```text
all_states
 ↓
["Alabama", "Alaska", ..., "Wyoming"]
```

`all_states` is used for validation, while `data` is used to find coordinates.

---

### Why `guessed_states` is a Separate List

`all_states` contains every possible answer.

`guessed_states` contains only the answers the player has already correctly entered.

```text
all_states
    ↓
Possible answers

guessed_states
    ↓
Already answered
```

This allows the program to prevent duplicate guesses.

---

# 🏗️ Program Structure

Although this project uses one main Python file, the logic can still be understood as separate responsibilities:

```text
                 U.S. States Game
                        │
        ┌───────────────┼───────────────┐
        │               │               │
      Turtle          Pandas        Game Logic
        │               │               │
      Map           CSV Data        Validation
      Input          States         Score
      Writing        Coordinates     Game Loop
```

Each technology has a clear role:

```text
Turtle
  ↓
Displays and interacts with the game

Pandas
  ↓
Reads and searches state data

Python
  ↓
Controls the game logic
```

---

# ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/MohammadMahroof/US-States-Game.git
```

### 2. Open the Project

Open the project folder in **VS Code**, **PyCharm**, or another Python IDE.

### 3. Run the Game

```bash
python main.py
```

The U.S. map will appear and the game will begin.

---

# 📋 Requirements

The project uses:

* Python
* Turtle
* Pandas

Install Pandas if required:

```bash
pip install pandas
```

`Turtle` is included with standard Python installations.

---

# 🚀 Future Improvements

Possible improvements for future versions:

* 📝 Generate a list of missed states when the player quits
* 💾 Save game progress
* 🏆 Add a high-score system
* 🎨 Improve the appearance of state labels
* 🔊 Add sound effects
* 🔄 Add a restart option
* ⏱️ Add a time limit
* 📊 Display additional game statistics
* 🗺️ Add support for other countries or maps

---

# 🎯 Learning Goal

The main goal of this project was to strengthen my understanding of **Python, Pandas, Turtle Graphics, and data-driven programming** by building an interactive application.

The project helped me understand how separate concepts can work together:

```text
Python Basics
      ↓
Lists & Conditions
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
Interactive Application
```

Instead of simply displaying data from a CSV file, the project uses that data to control the behavior and appearance of an interactive game.

---

# 📌 Project Status

**Completed** ✅

### Currently Implemented

* U.S. map display
* State data loading
* User input
* Input normalization
* State validation
* Duplicate prevention
* Coordinate lookup
* State name placement
* Score tracking
* Cancel button handling
* 50-state completion condition

---

# 👨‍💻 Author

**Mohammad Mahroof**

Python Developer | Software Developer

---

# 📝 Quick Repository Reminder

When I come back to this project later, I can quickly remember:

```text
main.py
    ↓
Controls the entire game

50_states.csv
    ↓
Contains state names and coordinates

blank_states_img.gif
    ↓
Provides the U.S. map
```

### Core Variables

```text
data
    → Complete Pandas DataFrame

all_states
    → List of all 50 states

guessed_states
    → Correct states guessed by the player

state_data
    → Data for the currently guessed state

state_turtle
    → Writes the state name on the map
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

### In One Sentence

> **Guess a valid U.S. state → find its coordinates → write it on the map → increase the score → repeat until all 50 states are found.**

---

## 📚 Part of My Python Learning Journey

This project represents another step in my journey of learning Python through **hands-on projects**.

The main focus was understanding how **Pandas data processing and Turtle graphics** can be combined with Python logic to create a complete interactive application.
.git
```

### 2. Open the Project

Open the project folder in **VS Code**, **PyCharm**, or another Python IDE.

### 3. Run the Game

```bash
python main.py
```

The U.S. map will appear and the game will begin.

---

# 📋 Requirements

The project uses:

* Python
* Turtle
* Pandas

Install Pandas if required:

```bash
pip install pandas
```

`Turtle` is included with standard Python installations.

---

# 🚀 Future Improvements

Possible improvements for future versions:

* 📝 Generate a list of missed states when the player quits
* 💾 Save game progress
* 🏆 Add a high-score system
* 🎨 Improve the appearance of state labels
* 🔊 Add sound effects
* 🔄 Add a restart option
* ⏱️ Add a time limit
* 📊 Display additional game statistics
* 🗺️ Add support for other countries or maps

---

# 🎯 Learning Goal

The main goal of this project was to strengthen my understanding of **Python, Pandas, Turtle Graphics, and data-driven programming** by building an interactive application.

The project helped me understand how separate concepts can work together:

```text
Python Basics
      ↓
Lists & Conditions
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
Interactive Application
```

Instead of simply displaying data from a CSV file, the project uses that data to control the behavior and appearance of an interactive game.

---

# 📌 Project Status

**Completed** ✅

### Currently Implemented

* U.S. map display
* State data loading
* User input
* Input normalization
* State validation
* Duplicate prevention
* Coordinate lookup
* State name placement
* Score tracking
* Cancel button handling
* 50-state completion condition

---

# 👨‍💻 Author

**Mohammad Mahroof**

Python Developer | Software Developer

---

# 📝 Quick Repository Reminder

When I come back to this project later, I can quickly remember:

```text
main.py
    ↓
Controls the entire game

50_states.csv
    ↓
Contains state names and coordinates

blank_states_img.gif
    ↓
Provides the U.S. map
```

### Core Variables

```text
data
    → Complete Pandas DataFrame

all_states
    → List of all 50 states

guessed_states
    → Correct states guessed by the player

state_data
    → Data for the currently guessed state

state_turtle
    → Writes the state name on the map
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

### In One Sentence

> **Guess a valid U.S. state → find its coordinates → write it on the map → increase the score → repeat until all 50 states are found.**

---

## 📚 Part of My Python Learning Journey

This project represents another step in my journey of learning Python through **hands-on projects**.

The main focus was understanding how **Pandas data processing and Turtle graphics** can be combined with Python logic to create a complete interactive application.
