# Sudoku
A simple algorithm for sudoku which shows basic front end and back end for the puzzle. 

# How it works:
## Backend
The Python script generates and solves Sudoku puzzles using the backtracking algorithm. It starts by creating a fully solved 9x9 Sudoku grid (generate_sudoku) and ensures it is valid (is_valid_sudoku). To create a playable puzzle, it removes 39 random numbers from the solved grid, leaving empty cells (emptyspaces). The script uses the is_safe function to check if placing a number in a cell complies with Sudoku rules (no duplicates in the row, column, or subgrid). The solve_sudoku function solves the grid recursively by filling in empty cells, backtracking when necessary. Finally, the program prints the generated Sudoku puzzle with empty cells (represented as 0).
## Frontend
The script uses tkinter for GUI.The frontend dynamically creates a 9x9 Sudoku grid where pre-filled numbers are displayed using labels, and empty cells are represented as entry fields for user input. The for_sudoku_grid function handles this by iterating over the grid and placing either a label (for fixed numbers) or an entry field (for empty cells) at each position. The entry fields are configured with validation logic to ensure that only numbers between 1 and 9, or an empty input, are accepted. This validation is achieved through the validate_input function, which is registered with each entry field and checks the input in real time, maintaining the integrity of the data entered by the user.

# Examples: 
![Image](https://github.com/user-attachments/assets/e069e93b-8f5c-4463-9323-2267cb2cfb3b)
![Image](https://github.com/user-attachments/assets/f2cc7ab5-0fee-4400-afac-cec3026239ad)

I was too lazy to actually play and show the output (results) page :)


## Note
No live error feedback is present in the program, meaning the user won't be able to know whether they have made error/s during their solving process until and unless the "check" button is clicked.

