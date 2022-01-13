# conway's game of life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# initialize a list of lists for the cells
next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        column.append(random.choice(('#',' ')))
    next_cells.append(column)

# game loop
while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells) # recursive?
    
    # print the current state
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print() # newline for each row
    
    # apply rules
    for x in range(WIDTH):
        for y in range(HEIGHT):

            # count neighbors
            neighbor_coords = {
                'topleft': ((x - 1) % WIDTH, (y - 1) % HEIGHT),
                'topcenter': (x, (y - 1) % HEIGHT),
                'topright': ((x + 1) % WIDTH, (y - 1) % HEIGHT),
                'centerleft': ((x - 1) % WIDTH, y),
                'centerright': ((x + 1) % WIDTH, y),
                'bottomleft': ((x - 1) % WIDTH, (y + 1) % HEIGHT),
                'bottomcenter': (x, (y + 1) % HEIGHT),
                'bottomright': ((x + 1) % WIDTH, (y + 1) % HEIGHT)
            }

            num_neighbors = 0
            for coord_x, coord_y in neighbor_coords.values():
                if current_cells[coord_x][coord_y] == '#':
                    num_neighbors += 1
            
            # set cell based on current state and neighbor count
            if (current_cells[x][y] == '#' and num_neighbors in (2,3)) or (current_cells[x][y] == ' ' and num_neighbors == 3):
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
    
    time.sleep(0.2)