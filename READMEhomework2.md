# ToggleIt: A Grid-Based Puzzle Game

## Overview
**ToggleIt** is a puzzle game where the goal is to toggle cells in a grid to turn all cells into "0". Each move toggles a selected cell and its neighbors (up, down, left, right). The game supports customizable grid sizes and allows testing different heuristics for solving the puzzle.

## Key Classes and Methods

### `ToggleIt`
This is the base class for the game.

#### Attributes:
- **`size`**: The size of the grid (e.g., 3 for a 3x3 grid).
- **`initial`**: Starting state of the grid (random or user-defined).
- **`goal`**: The target state where all cells are "0".

#### Methods:
- **`showBoard()`**: Displays the current grid in a readable format.
- **`goal_test(state)`**: Checks if the state matches the goal.
- **`actions(state)`**: Returns a list of valid cell indices to toggle.
- **`result(state, action)`**: Toggles a cell and its neighbors to generate a new state.
- **`switch(num)`**: A helper function to toggle a cell between "0" and "1".

### `ToggleIt_optimal`
A subclass of `ToggleIt` that uses an **optimal heuristic** to estimate the fewest moves needed to solve the puzzle.

### `ToggleIt_suboptimal`
A subclass of `ToggleIt` that uses a **simple heuristic** based on the count of "1"s in the grid.

## State Representation
- The grid is represented as a single string of "0"s and "1"s.
- Example for a 3x3 grid:
  ```
  "010101010"  (read row by row)
  ```

## Example Usage
1. Create a game instance:
   ```python
   game = ToggleIt_optimal(3)
   print(game.showBoard())
   ```

2. Check if the initial state is the goal:
   ```python
   print(game.goal_test(game.initial))
   ```

3. Toggle a cell and view the updated grid:
   ```python
   game.result(game.initial, 4)  # Toggle cell at index 4
   print(game.showBoard())
   ```
