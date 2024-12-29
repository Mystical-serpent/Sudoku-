import tkinter as tts
from sudoku import generate_sudoku, emptyspaces #this may cause an error as "sudoku" library may not be present
import numpy as np

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
                                 background="Green")
        label_result.pack()
    else:
        label_result = tts.Label(Window_pop_up,
                                 text="The Grid is Invalid",
                                 font=("Calibri", 19),
                                 background="Red")
        label_result.pack()
    
    button_exit = tts.Button(Window_pop_up, text="Exit",
                             font=("Calibri", 18), 
                             command=lambda: [Window_pop_up.quit(), Window.quit()])
    button_exit.pack()

# Main Tkinter window
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
