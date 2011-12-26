def parse(grid):
    ''' Parses a Sudoku grid by converting it from xxx...x..xx....xx format to a friendly-looking grid. 
    
    Sample input: ...5.14582.14.28.1.99128.9..2....992...536..89.8....7.....1..9.93.3.9..219.....7.
    Sample output: 
    
    . . . | 5 . 1 | 4 5 8 
    2 . 1 | 4 . 2 | 8 . 1 
    . 9 9 | 1 2 8 | . 9 . 
    - - - - - - - - - - - 
    . 2 . | . . . | 9 9 2 
    . . . | 5 3 6 | . . 8 
    9 . 8 | . . . | . 7 . 
    - - - - - - - - - - - 
    . . . | . 1 . | . 9 . 
    9 3 . | 3 . 9 | . . 2
    1 9 . | . . . | . 7 . 
    
    Note: it tends to print None after the last row for some reason. I still haven't pinpointed
          the cause of this behavior. '''
    
    # First part. Adds pipes and hyphens to inputted string to seperate boxes in the grid.
    old = list(grid)
    new = []
    count = 1
    for one in old:
        new.append(one)
        if count % 3 == 0 and count % 9 != 0:
            new.append('|')
        if count % 27 == 0 and count < 81:
            [new.append('-') for i in range(1, 12)]
        count += 1
    
    grid = ''.join(new)
    
    # Second part. Prints out a nice grid from the result above.
    row = []
    col = 0
    for one in grid:
        row.append(one + ' ')
        col += 1
        if col == 11:
            print ''.join(row)
            col = 0
            row = []
    
grid = '...5.14582.14.28.1.99128.9..2....992...536..89.8....7.....1..9.93.3.9..219.....7.'
print parse(grid)