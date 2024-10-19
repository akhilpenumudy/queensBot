# Queens Solver

## About the Project

Queens Solver is a Python application that allows users to play and solve the Queens puzzle game. This project provides a graphical user interface for creating custom Queens puzzles and an algorithm to solve them automatically.

## The Queens Game

Queens is a logic puzzle game created by LinkedIn. The objective is to place queens on a grid such that:

1. Each row contains exactly one queen
2. Each column contains exactly one queen
3. Each colored region contains exactly one queen
4. No two queens can attack each other (i.e., they cannot be in the same row, column, or diagonal)

For more information about the original game, visit the [official Queens game page](https://www.linkedin.com/games/queens/).

## Features

- Interactive GUI for creating custom Queens puzzles
- Customizable grid size (up to 20x20)
- 13 different colors for creating unique regions
- Automatic puzzle solver

## How It Works

### GUI (imageProcessing.py)

The graphical user interface is built using Python's Tkinter library. It allows users to:

1. Create a grid of custom size
2. Select colors and paint regions on the grid
3. Trigger the solving algorithm
4. Visualize the solution

### Solving Algorithm (queens_solver.py)

The solving algorithm uses a backtracking approach with the following key features:

1. **Color Region Tracking**: The algorithm groups cells by color to ensure each region contains exactly one queen.

2. **Safety Checking**: Before placing a queen, the algorithm checks if the placement is safe by ensuring:

   - No other queen is in the same row or column
   - No other queen is in any diagonal
   - No other queen is in an adjacent cell (including diagonally)

3. **Backtracking**: If a safe placement is not found, the algorithm backtracks and tries different configurations until a solution is found or all possibilities are exhausted.

## How to Use

1. Run `imageProcessing.py`
2. Click "Create Grid" and enter the desired grid size
3. Use the color buttons to paint regions on the grid
4. Click "Solve" to find a solution
5. The solution will be displayed on the grid with crown emojis (👑)

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Future Improvements

- Add a feature to input puzzles from the official Queens game
- Implement an option to generate random puzzles
- Optimize the solving algorithm for larger grid sizes

## Contributing

Contributions to improve the Queens Solver are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-source and available under the MIT License.
