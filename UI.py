import tkinter as tts


def create_start_window(start_callback, exit_callback):
    #Creates the start-up window.
    start_window = tts.Tk()
    start_window.title("Sudoku")
    start_window.geometry("700x500")

    label_for_start = tts.Label(
        start_window, text="SUDOKU", font=("Calibri", 30)
    )
    label_for_start.pack(pady=35)

    button_frame = tts.Frame(start_window)
    button_frame.pack(pady=20)

    button_to_play = tts.Button(
        button_frame,
        text="Play",
        font=("Calibri", 18),
        width=10,
        background="Green",
        command=start_callback,
    )
    button_to_play.grid(row=0, column=0, padx=20)

    button_to_exit = tts.Button(
        button_frame,
        text="Exit",
        width=10,
        font=("Calibri", 18),
        background="Red",
        command=exit_callback,
    )
    button_to_exit.grid(row=0, column=1, padx=20)

    return start_window


def create_main_window(check_callback):
    #Creates the main Sudoku window.
    main_window = tts.Tk()
    main_window.title("Sudoku")
    main_window.geometry("800x600")

    label = tts.Label(main_window, text="Try out this Problem", font=("Calibri", 20))
    label.pack(padx=14, pady=18)

    grid_frame = tts.Frame(main_window)
    grid_frame.pack()

    return main_window, grid_frame


def display_result(message, color, play_again_callback, exit_callback):
    #Creates a pop-up window to display the result
    result_window = tts.Tk()
    result_window.title("Results")
    result_window.geometry("350x200")

    label_result = tts.Label(
        result_window, text=message, font=("Calibri", 19), fg=color, pady=20
    )
    label_result.pack()

    button_play_again = tts.Button(
        result_window,
        text="Play Again",
        font=("Calibri", 18),
        background="Green",
        command=play_again_callback,
    )
    button_play_again.pack(pady=10)

    button_exit = tts.Button(
        result_window,
        text="Exit",
        font=("Calibri", 18),
        background="Red",
        command=exit_callback,
    )
    button_exit.pack(pady=10)

    return result_window


def create_sudoku_grid(window, sudoku, validate_command):
    #Creates the grid UI for Sudoku.
    inputs_all = []

    for row in range(9):
        row_entries = []
        for column in range(9):
            specific_val = sudoku[row][column]
            if specific_val != 0:
                label_grid = tts.Label(
                    window,
                    text=str(specific_val),
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
                    window,
                    font=("Calibri", 15),
                    width=3,
                    relief="solid",
                    borderwidth=1,
                    justify="center",
                    validate="key",
                    validatecommand=validate_command,
                )
                entry_inputs.grid(row=row, column=column, padx=1, pady=1)
                row_entries.append(entry_inputs)
        inputs_all.append(row_entries)
    return inputs_all
