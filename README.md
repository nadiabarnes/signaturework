# signaturework
This is to fulfill the signature work requirement for CISC Senior Capstone

# ToggleIt: A Grid-Based Puzzle Game

## Overview
**ToggleIt** is a grid-based puzzle game implemented as a search problem. The objective is to toggle cells in a grid between "0" and "1" to achieve a state where all cells are "0". Each action toggles a selected cell and its adjacent neighbors (top, bottom, left, and right). The game supports customizable grid sizes and provides functionality to solve the puzzle using search algorithms.

## Classes and Functionality

### `ToggleIt` Class
This class represents the base ToggleIt puzzle and inherits from `search.Problem`.

#### Key Attributes:
- **`size`**: The grid size (e.g., `size=3` creates a 3x3 grid).
- **`initial`**: The initial state of the grid, represented as a string of "0" and "1".
- **`goal`**: The goal state, where all cells are "0".
- **`current`**: Tracks the current state for visualization during testing.

#### Key Methods:
- **`__init__(size, initial=None, goal=None)`**: Initializes the grid size, initial state, and goal state. If no initial state is provided, it generates a random starting state.
- **`showBoard()`**: Displays the current state of the grid in a readable format.
- **`goal_test(state)`**: Checks if the given state matches the goal state.
- **`actions(state)`**: Generates all valid actions (indices of the grid cells).
- **`result(state, action)`**: Applies an action (toggling the selected cell and its neighbors) to generate a new state.
- **`path_cost(c, state1, action, state2)`**: Defines the cost of transitioning between states (always 1 per action).
- **`switch(num)`**: Helper method to toggle a cell between "0" and "1".

---

### `ToggleIt_optimal` Class
This class inherits from `ToggleIt` and implements an **optimal heuristic** to estimate the shortest path to the goal.

#### Key Method:
- **`h(node)`**: Calculates the heuristic value by:
  - Counting the number of "1"s in the current state.
  - Dividing the count by the maximum number of "1"s that can be toggled off in a single action, adjusted for grid size.
  - Returns the ceiling of this value as the estimated cost.

---

### `ToggleIt_suboptimal` Class
This class inherits from `ToggleIt` and implements a **suboptimal heuristic** for comparison purposes.

#### Key Method:
- **`h(node)`**: Calculates the heuristic value by counting the total number of "1"s in the current state. This heuristic is less effective than the optimal one.

---

## State Representation
- A grid state is represented as a string of length `size**2`.
  - Each character is either "0" or "1".
  - The grid is read row by row, left to right.
- Example for a 3x3 grid:
  ```
  Initial State: "010101010"
  Goal State:    "000000000"
  ```

## Actions
- An action corresponds to toggling a specific cell.
- Each action also toggles the cell's neighbors (if within grid boundaries).

## Testing
The provided code includes a commented-out section for testing:
- Initializing a grid.
- Displaying the grid.
- Verifying if the initial state matches the goal.
- Generating possible actions.
- Applying an action to see the resulting state.
- Calculating heuristic values for the current state.

Example:
```python
# Testing ToggleIt_optimal
board = ToggleIt_optimal(3)
print(board.showBoard())
print("Goal Test:", board.goal_test(board.initial))
print("Actions:", board.actions(board.initial))
board.result(board.initial, 4)  # Apply action at index 4
print(board.showBoard())
```

## Requirements
- Python 3.x
- `math`, `random`, and `collections` modules (standard library)
- `search` module (assumed to provide the `Problem` and `Node` classes)

## Heuristics Comparison
- **Optimal Heuristic**:
  - More accurate and admissible.
  - Considers the maximum potential toggles per action based on grid size.
- **Suboptimal Heuristic**:
  - Simple but less effective.
  - Directly counts the number of "1"s in the current state.

## Future Enhancements
- Integrate a search algorithm (e.g., A*) to solve the puzzle automatically.
- Expand testing for larger grid sizes.
- Add visualization tools for better understanding of state transitions.
