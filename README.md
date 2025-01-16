# Sudoku
A simple algorithm for sudoku which shows basic front end and back end for the puzzle. 
Uses tkinter for the UI and numpy is used to generate the grid. The program generates a random grid with 38 randomly determined "empty slots" where the user fills what they think will be the correct number there. Back tracking is present for verification of each grid generated to always print out valid grids which follow the rules of the puzzle. 

No live error feedback is present in the program, meaning the user won't be able to know whether they have made error/s during their solving process until and unless the "check" button is clicked. After that, each input in the entries (tkinter widget) will be checked. 

Note: when back tracking is happening, the index of empty slots (0) are stored. This makes such that when the check button is clicked, only the inputted data is stored with the stored data, making the program more efficient. 
