# Written by: Assil Ksiksi
# Date: Decemeber 21st, 2011

# A simple script that "splices" a Sudoku grid into 9 3x3 boxes. A similar method
# may be included in my Sudoku solver to determine whether or not a number can
# be placed in a certain cell. Should also be applicable to rows and columns.

from random import seed, choice

def create_grid():
    ''' Randomly generates a 9x9 multi-dimensional "pseudo-Sudoku grid" in list format. '''
    grid = []
    row = []
    choices = '123456789............'
    for i in range(9):
        for j in range(9):
            seed(None)
            row.append(choice(choices))
        grid.append(row)
        row = []
    return grid

def format_box(box, count):
    ''' Formats each box from a 9x9 Sudoku grid and adds a box #. '''
    new = []
    new.append('Box #{}'.format(count) + '\n')
    for i in box:
        for j in i:
            new.append(j + ' ')
        new.append('\n')
    return ''.join(new)

def splice_grid():
    ''' Splices a 9x9 Sudoku grid, and prints out the boxes that form it. 
        
        Runtime: ~0.035s'''
    grid = create_grid()
    boxes = []
    row = 3 # Used to determine where splicing should occur.
    col = 3
    count = 1
    for i in range(3): # Used to keep count of row number
        for j in range(3): # Creates boxes for each row
            boxes.append([x[col-3:col] for x in grid[row-3:row]]) # Nifty list comprehension that splices a multi-dimensional list.
            col += 3
        for k in boxes: # Sifts through boxes in each row, and passes them to format_box
            print format_box(k, count)
            count += 1
        boxes = []
        col = 3
        row += 3

splice_grid()