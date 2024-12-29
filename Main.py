import tkinter as tts
import numpy as np
import random

def for_sudoku_grid(Window, sudoku):
    inputs_all = []
    
    def validate_input(input_entry):
        if input_entry == "" or (input_entry.isdigit() and 1 <= int(input_entry) <= 9):
            return True
        return False

    vcmd = (Window.register(validate_input), "%P")

    for row in range(9):
        row_entries = []
        for column in range(9):
            Specific_val = sudoku[row][column]
            if Specific_val != 0:
                label_grid = tts.Label(Window, 
                                       text=str(Specific_val),
                                       font=("Calibri", 15),
                                       width=3,
                                       height=1,
                                       relief="solid",
                                       borderwidth=0.8, 
                                       bg="lightgrey")
                label_grid.grid(row=row,
                                column=column, 
                                padx=1, 
                                pady=1)
            else:
                entry_inputs = tts.Entry(
                    Window, 
                    font=("Calibri", 15), 
                    width=3,
                    relief="solid",
                    borderwidth=1,
                    justify="center",
                    validate="key",
                    validatecommand=vcmd
                )
                entry_inputs.grid(row=row, 
                                  column=column, 
                                  padx=1, 
                                  pady=1)
                row_entries.append(entry_inputs)
        inputs_all.append(row_entries)
    return inputs_all

def validate_the_grid(inputs_all, Empty_index_store, original_grid):
    Window_pop_up = tts.Tk()
    Window_pop_up.title('Results')
    Window_pop_up.geometry("350x350")

    temp_original_od = np.array(original_grid).copy().flatten()
    Actual_value_list = []
    empty_index = 0
    while empty_index < len(Empty_index_store):
        Actual_value_list.append(temp_original_od[Empty_index_store[empty_index]])
        empty_index += 1 
    
    flattened_inputs = [entry.get() for row in inputs_all for entry in row]

    if flattened_inputs == Actual_value_list:
        label_result = tts.Label(Window_pop_up, 
                                 text="The Grid is Valid, Good job!", 
                                 font=("Calibri", 19), 
                                 background="Green",
                                 pady=20)
        label_result.pack()
    else:
        label_result = tts.Label(Window_pop_up,
                                 text="The Grid is Invalid",
                                 font=("Calibri", 19),
                                 background="Red",
                                 pady=20)
        label_result.pack()
    
    button_exit = tts.Button(Window_pop_up, text="Exit",
                             font=("Calibri", 18), 
                             command=lambda: [Window_pop_up.quit(), Window.quit()])
    button_exit.pack(pady=30)

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
    Empty_index_store = []
    temp_matrix = np.copy(sudoku_table_no_spaces).flatten()
    while count < 39:
        random_empty_index = random.randint(0, 80)
        if temp_matrix[random_empty_index] != 0:
            temp_matrix[random_empty_index] = 0
            Empty_index_store.append(random_empty_index)
            count += 1
    grid_spaces_sudoku = temp_matrix.reshape(9, 9)
    return grid_spaces_sudoku, Empty_index_store

Window = tts.Tk()
Window.title('Sudoku')
Window.geometry("800x600")

label = tts.Label(Window, text="Try out this Problem", font=('Calibri', 20))
label.pack(padx=14, pady=18)

Frames_of_the_grid = tts.Frame(Window)
Frames_of_the_grid.pack()

sudoku_table_no_spaces = generate_sudoku()
sudoku_table_spaces, Empty_index_store = emptyspaces(sudoku_table_no_spaces)

inputs_all = for_sudoku_grid(Frames_of_the_grid, sudoku_table_spaces)

check_button = tts.Button(Window, text="Check", font=("Calibri", 15), command=lambda: validate_the_grid(inputs_all, Empty_index_store, sudoku_table_no_spaces))
check_button.pack(pady=30)

Window.mainloop()
