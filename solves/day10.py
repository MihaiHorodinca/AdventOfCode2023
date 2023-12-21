from enum import Enum


class Direction(Enum):
    North = (-1, 0)
    South = (1, 0)
    East = (0, 1)
    West = (0, -1)


oppositeDirections = {
    Direction.North: Direction.South,
    Direction.South: Direction.North,
    Direction.West: Direction.East,
    Direction.East: Direction.West
}


pieces = {
    '.': [],
    '|': [Direction.North, Direction.South],
    '-': [Direction.West, Direction.East],
    'L': [Direction.North, Direction.East],
    'J': [Direction.North, Direction.West],
    '7': [Direction.West, Direction.South],
    'F': [Direction.East, Direction.South]
}


SHAPES_ZOOMED = {
    '.': [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]],
    '|': [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]],
    '-': [[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]],
    'L': [[0, 1, 0],
          [0, 1, 1],
          [0, 0, 0]],
    'J': [[0, 1, 0],
          [1, 1, 0],
          [0, 0, 0]],
    '7': [[0, 0, 0],
          [1, 1, 0],
          [0, 1, 0]],
    'F': [[0, 0, 0],
          [0, 1, 1],
          [0, 1, 0]]
}


def get_input():
    fileName = "day10input.txt"
    with open(fileName, 'r') as myFile:
        return myFile.readlines()


pipeMap = get_input()
zoomedPipeMap = [[0] * (len(pipeMap[0]) * 3) for a in range(0, len(pipeMap) * 3 + 1)]


def draw_zoomed_piece(position: (int, int), piece: str = None):
    if piece is None:
        piece = pipeMap[position[0]][position[1]]

    zoomedTopLeftPosition = (position[0] * 3, position[1] * 3)
    zoomedPiece = SHAPES_ZOOMED.get(piece)

    for change1 in range(0, 3):
        for change2 in range(0, 3):
            zoomedPipeMap[zoomedTopLeftPosition[0] + change1][zoomedTopLeftPosition[1] + change2] = zoomedPiece[change1][change2]


def draw_starting_piece_zoomed(position: (int, int), direction1: Direction, direction2: Direction):
    for piece in pieces.items():
        if direction1 in piece[1] and direction2 in piece[1]:
            draw_zoomed_piece(position, piece[0])


def find_starting_directions(startX, startY):
    pipes = []

    for direction in Direction:
        diffX, diffY = direction.value
        oppositeDirection = oppositeDirections.get(direction)
        newX = startX + diffX
        newY = startY + diffY

        print(pipeMap[newX][newY])
        print(pieces.get(pipeMap[newX][newY]))
        if pieces.get(pipeMap[newX][newY]).__contains__(oppositeDirection):
            pipes.append(((newX, newY), oppositeDirection))

    if len(pipes) == 2:
        return pipes
    else:
        print("There should be only 2 possible continuations from the start.")


def move_forward(position: (int, int), inputDirection: Direction):
    draw_zoomed_piece(position)

    print(f'Moving into position {position} and coming from {inputDirection.name}')
    currentPiece = pipeMap[position[0]][position[1]]
    pieceDirections = pieces.get(currentPiece)

    exitDirection = [direction for direction in pieceDirections if direction != inputDirection][0]
    print(f'Will go towards {exitDirection.name}')

    newPosition = tuple(a+b for a, b in zip(position, exitDirection.value))
    newInputDirection = oppositeDirections.get(exitDirection)
    print(f'New pos id {newPosition} with input direction {newInputDirection.name}')
    print()

    return newPosition, newInputDirection


# The recursive method failed due to exceeding Python's maximum recursion depth limit.
def fill_outside_rec(position: (int, int)):
    for direction in Direction:
        newPosition = (position[0] + direction.value[0], position[1] + direction.value[1])

        if 0 <= newPosition[0] < len(zoomedPipeMap) and \
                0 <= newPosition[1] < len(zoomedPipeMap[0]) and \
                zoomedPipeMap[newPosition[0]][newPosition[1]] == 0:
            zoomedPipeMap[newPosition[0]][newPosition[1]] = -1
            fill_outside_rec(newPosition)


def fill_outside():
    positionsToCheck = set()
    positionsToCheck.add((0, 0))

    while len(positionsToCheck) > 0:
        position = positionsToCheck.pop()
        for direction in Direction:
            newPosition = (position[0] + direction.value[0], position[1] + direction.value[1])

            if 0 <= newPosition[0] < len(zoomedPipeMap) and \
                    0 <= newPosition[1] < len(zoomedPipeMap[0]) and \
                    zoomedPipeMap[newPosition[0]][newPosition[1]] == 0:
                zoomedPipeMap[newPosition[0]][newPosition[1]] = -1
                positionsToCheck.add(newPosition)


def find_positions_inside():
    total = 0
    for X in range(1, len(zoomedPipeMap), 3):
        for Y in range(1, len(zoomedPipeMap[0]), 3):
            if zoomedPipeMap[X][Y] == 0:
                total += 1
    return total


def solve():
    startX, startY = 0, 0

    for index, line in enumerate(pipeMap):
        if 'S' in line:
            startX = index
            startY = line.index('S')
            break

    print(f'Starting from {startX}, {startY}')

    (position1, direction1), (position2, direction2) = find_starting_directions(startX, startY)
    print(f'Found continuations towards {direction1.name} and {direction2.name}')

    draw_starting_piece_zoomed((startX, startY),
                               oppositeDirections.get(direction1), oppositeDirections.get(direction2))

    steps = 1
    while position1 != position2:
        position1, direction1 = move_forward(position1, direction1)
        position2, direction2 = move_forward(position2, direction2)
        steps += 1

    draw_zoomed_piece(position1)
    fill_outside()
    print(find_positions_inside())

    print(position1)
    print(steps)

    for line in zoomedPipeMap:
        print(line)


solve()
