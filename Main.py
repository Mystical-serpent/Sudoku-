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
                label_grid = tts.Label(
                    Window,
                    text=str(Specific_val),
                    font=("Calibri", 15),
                    width=3,
                    height=1,
                    relief="solid",
                    borderwidth=0.8,
                    bg="lightgrey",
                )
                label_grid.grid(row=row, column=column, padx=1, pady=1)
                row_entries.append(None)
            else:
                entry_inputs = tts.Entry(
                    Window,
                    font=("Calibri", 15),
                    width=3,
                    relief="solid",
                    borderwidth=1,
                    justify="center",
                    validate="key",
                    validatecommand=vcmd,
                )
                entry_inputs.grid(row=row, column=column, padx=1, pady=1)
                row_entries.append(entry_inputs)
        inputs_all.append(row_entries)
    return inputs_all

def validate_the_grid(inputs_all, Empty_index_store, original_grid, Window):
    user_inputs = np.zeros((9, 9), dtype=int)
    for i, row in enumerate(inputs_all):
        for j, entry in enumerate(row):
            if entry is not None and entry.get().isdigit():
                user_inputs[i][j] = int(entry.get())
            else:
                user_inputs[i][j] = 0

    original_solution = np.array(original_grid).flatten()
    user_solution = user_inputs.flatten()

    expected_values = [original_solution[idx] for idx in Empty_index_store]
    user_values = [user_solution[idx] for idx in Empty_index_store]

    if user_values == expected_values:
        result_message = "The Grid is Valid, Good job!"
        result_color = "green"
    else:
        result_message = "The Grid is Invalid. Try Again!"
        result_color = "red"

    Window.destroy()
    Window_pop_up = tts.Tk()
    Window_pop_up.title("Results")
    Window_pop_up.geometry("350x200")

    label_result = tts.Label(
        Window_pop_up,
        text=result_message,
        font=("Calibri", 19),
        fg=result_color,
        pady=20,
    )
    label_result.pack()

    button_play_again = tts.Button(
        Window_pop_up,
        text="Play Again",
        font=("Calibri", 18),
        background="Green",
        command=lambda: [Window_pop_up.destroy(), main_window()],
    )
    button_play_again.pack(pady=10)

    button_exit = tts.Button(
        Window_pop_up,
        text="Exit",
        font=("Calibri", 18),
        background="Red",
        command=Window_pop_up.quit,
    )
    button_exit.pack(pady=10)

    Window_pop_up.mainloop()

def is_safe(grid, row, col, num):
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    return (
        num not in grid[row, :]
        and num not in grid[:, col]
        and num not in grid[subgrid_row : subgrid_row + 3, subgrid_col : subgrid_col + 3]
    )

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)  # Shuffle numbers to add randomness
                for num in nums:
                    if is_safe(grid, row, col, num):
                        grid[row, col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row, col] = 0
                return False
    return True

def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    
    # Randomly fill a few cells to introduce variability
    for _ in range(random.randint(10, 15)):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_safe(grid, row, col, num):
            grid[row, col] = num
    
    solve_sudoku(grid)  # Solve the Sudoku starting from the partially filled grid
    return grid

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

def main_window():
    Window = tts.Tk()
    Window.title("Sudoku")
    Window.geometry("800x600")

    label = tts.Label(Window, text="Try out this Problem", font=("Calibri", 20))
    label.pack(padx=14, pady=18)

    sudoku_table_no_spaces = generate_sudoku()
    sudoku_table_spaces, Empty_index_store = emptyspaces(sudoku_table_no_spaces)

    Frames_of_the_grid = tts.Frame(Window)
    Frames_of_the_grid.pack()

    inputs_all = for_sudoku_grid(Frames_of_the_grid, sudoku_table_spaces)

    check_button = tts.Button(
        Window,
        text="Check",
        font=("Calibri", 15),
        command=lambda: validate_the_grid(inputs_all, Empty_index_store, sudoku_table_no_spaces, Window),
    )
    check_button.pack()

    Window.mainloop()

def Start_up_window():
    Start_window = tts.Tk()
    Start_window.title("Sudoku")
    Start_window.geometry("700x500")

    label_for_Start = tts.Label(
        Start_window, text="SUDOKU", font=("Calibri", 30)
    )
    label_for_Start.pack(pady=35)

    button_frame = tts.Frame(Start_window)
    button_frame.pack(pady=20)

    Button_to_play = tts.Button(
        button_frame,
        text="Play",
        font=("Calibri", 18),
        width=10,
        background="Green",
        command=lambda: [Start_window.destroy(), main_window()],
    )
    Button_to_play.grid(row=0, column=0, padx=20)

    Button_to_exit = tts.Button(
        button_frame,
        text="Exit",
        width=10,
        font=("Calibri", 18),
        background="Red",
        command=Start_window.quit,
    )
    Button_to_exit.grid(row=0, column=1, padx=20)

    Start_window.mainloop()

Start_up_window()
