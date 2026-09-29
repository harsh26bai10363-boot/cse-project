  Cricket Scoreboard

A menu-driven Python project created for the **Python Essentials – Evaluated Course Project**.

 Project Overview

The Cricket Scoreboard is a command-line application that records and analyzes the batting performance of players in a cricket match.

The program allows the user to:

- Set up a match
- Add players
- Assign batting positions
- Record runs, balls, fours and sixes
- Mark players as Out or Not Out
- View a complete scoreboard
- Calculate team statistics
- Find the highest scorer
- Find the lowest scorer
- Search for a player
- Find the boundary leader
- View player information
- Reset the match

 Objectives

1. Apply fundamental Python programming concepts to a practical problem.
2. Store and manipulate structured data using Python collections.
3. Use loops and conditional statements to process player statistics.
4. Divide a larger problem into smaller functions.
5. Implement basic searching, counting, maximum and minimum algorithms.

 Python Concepts Used

This project is intentionally designed around introductory Python concepts:

- Variables
- Data types
- Input and output
- Arithmetic operators
- Comparison operators
- Logical operators
- Conditional statements
- `for` loops
- `while` loops
- `break`
- Functions
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Basic algorithms

 Data Structures

### Dictionary

Player statistics are stored using a nested dictionary:

```python
players[name] = {
    "position": position,
    "runs": 0,
    "balls": 0,
    "fours": 0,
    "sixes": 0,
    "out": "Not Out"
}
```

 List

`player_order` maintains the order in which players were added.

 Set

`player_names` stores unique player names and makes player-existence checking simple.

 Tuple

`batting_positions` stores the fixed set of available batting positions.

 How to Run

### Requirements

- Python 3.x
- VS Code or another Python IDE

Steps

1. Download or clone the repository.
2. Open the folder in VS Code.
3. Open `main.py`.
4. Run the program.

```bash
python main.py
```

 Main Menu

```text
1. Add Player
2. Record Player Performance
3. View Scoreboard
4. View Team Statistics
5. Find Highest Scorer
6. Find Lowest Scorer
7. Search Player
8. Find Boundary Leader
9. Display Player List
10. Display Match Information
11. Reset Match
12. Exit
```

 Example

Suppose the following players are entered:

| Player | Runs | Balls | 4s | 6s | Status |
|---|---:|---:|---:|---:|---|
| Rohit | 72 | 45 | 8 | 2 | Out |
| Virat | 95 | 58 | 9 | 3 | Not Out |
| Rahul | 34 | 30 | 4 | 0 | Out |
| Surya | 56 | 32 | 5 | 2 | Out |

The program can calculate the team score, wickets, average, boundary count and current run rate.

 Testing

The program should be tested for:

1. Adding a valid player.
2. Trying to add a duplicate player.
3. Recording valid performance.
4. Entering negative statistics.
5. Entering too many boundary runs.
6. Viewing the scoreboard before adding players.
7. Searching for an existing player.
8. Searching for a player who does not exist.
9. Finding highest and lowest scorers.
10. Resetting the match.
11. Exiting through the menu.

 Limitations

- Data is stored only while the program is running.
- It currently focuses on batting statistics.
- There is no graphical interface.
- There is no permanent database or file storage.
- Advanced match features such as ball-by-ball simulation are not included.

 Future Scope

After learning additional Python concepts, the project can be extended with:

- File handling for permanent storage
- Ball-by-ball match simulation
- Bowling statistics
- Strike rate and economy rate
- Target calculation
- Multiple innings
- Match result calculation
- Graphical charts
- GUI
- Object-oriented programming

 Author

College Student Python Project

Created as part of the Python Essentials evaluated course project.
