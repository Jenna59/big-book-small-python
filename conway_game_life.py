import copy, random, sys, time

WIDTH = 79
HEIGHT = 20

ALIVE = '|'
DEAD = '_'

nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    print('\n' * 10) # separate each step with new lines
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press CTRL+D to quit.')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # top-left neighbor is alive
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # top neighbor is alive
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # top-right neighbor is alive
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # left neighbor is alive
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1 # right neighbor is alive
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # bottom-left neighbor is alive
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1 # bottom neighbor is alive
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # bottom-right neighbor is alive

            # Set character in the cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1) # 1 second pause to reduce screen flicker
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()
