import numpy as np
import random

def is_safe(grid, row, col, num):
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    return (num not in grid[row, :] and
            num not in grid[:, col] and
            num not in grid[subgrid_row:subgrid_row+3, subgrid_col:subgrid_col+3])

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row, col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row, col] = 0
                return False
    return True

def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    return grid

def is_valid_sudoku(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row, col]
            if num != 0:
                grid[row, col] = 0  
                if not is_safe(grid, row, col, num):
                    return False
                grid[row, col] = num  
    return True

def emptyspaces(sudoku_table_no_spaces):
    count = 0
    temp_matrix = np.copy(sudoku_table_no_spaces).flatten()  
    while count < 39:
        random_empty_index = random.randint(0, 80)
        if temp_matrix[random_empty_index] != 0:  
            temp_matrix[random_empty_index] = 0  
            count += 1
    grid_spaces_sudoku = temp_matrix.reshape(9, 9)  
    return grid_spaces_sudoku

def generate_valid_sudoku():
    while True:
        grid = generate_sudoku()
        if is_valid_sudoku(grid):
            return grid

sudoku_table_no_spaces = generate_valid_sudoku()
sudoku_table_spaces = emptyspaces(sudoku_table_no_spaces)
print(sudoku_table_spaces)

