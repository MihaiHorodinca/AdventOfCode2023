fileName = "day3input.txt"
directionsFirstDigit = [(-1, -1), (0, -1), (1, -1)]
directionsEveryDigit = [(-1, 0), (1, 0)]
directionsLastDigit = [(-1, 0), (0, 0), (1, 0)]

directionsForGears = [(-1, 0), (0, 0), (1, 0)]

myFile = open(fileName, "r")
engineSchematic = myFile.readlines()
noLines = len(engineSchematic)
noColumns = len(engineSchematic[0].strip())

gearSchematic = [[(0, 1) for _ in range(noColumns)] for _ in range(noLines)]


def is_symbol(char):
    return not (char.isdigit() or char == ".")


def look_near(lineIndex: int, columnIndex: int, direction: (int, int)):
    lineDirection, columnDirection = direction
    return engineSchematic[min(max(lineIndex + lineDirection, 0), noLines - 1)][
        min(max(columnIndex + columnDirection, 0), noColumns - 1)]


def touches_symbol(lineIndex, columnIndex, directions):
    for direction in directions:
        if is_symbol(look_near(lineIndex, columnIndex, direction)):
            return True
    return False


def solve_a():
    partSum = 0
    for lineIndex, line in enumerate(engineSchematic):
        line = line.strip()
        currentNumber = ""
        isPartNumber = False

        for columnIndex, char in enumerate(line):
            if char.isdigit():
                if len(currentNumber) == 0:
                    isPartNumber |= touches_symbol(lineIndex, columnIndex, directionsFirstDigit)
                isPartNumber |= touches_symbol(lineIndex, columnIndex, directionsEveryDigit)

                currentNumber += char
            else:
                if len(currentNumber) > 0:
                    isPartNumber |= touches_symbol(lineIndex, columnIndex, directionsLastDigit)
                    partSum += int(currentNumber) if isPartNumber else 0
                    currentNumber = ""
                    isPartNumber = False

        partSum += int(currentNumber) if isPartNumber else 0
    print(partSum)


def update_near(lineIndex, columnIndex, partNumber):
    for direction in directionsForGears:
        lineDirection, columnDirection = direction
        newLineIndex = lineIndex + lineDirection
        newColumnIndex = columnIndex + columnDirection

        if 0 <= newLineIndex < noLines and 0 <= newColumnIndex < noColumns and engineSchematic[newLineIndex][newColumnIndex] == "*":
            gear = gearSchematic[newLineIndex][newColumnIndex]
            gearSchematic[newLineIndex][newColumnIndex] = (gear[0] + 1, gear[1] * partNumber)


def update_gears(lineIndex, columnIndex, partNumber):
    while columnIndex >= 0:
        update_near(lineIndex, columnIndex, partNumber)
        columnIndex -= 1

        if not engineSchematic[lineIndex][columnIndex].isdigit():
            break
    update_near(lineIndex, columnIndex, partNumber)


def solve_b():
    for lineIndex, line in enumerate(engineSchematic):
        line = line.strip()
        currentNumber = ""

        for columnIndex, char in enumerate(line):
            if char.isdigit():
                currentNumber += char
            else:
                if len(currentNumber) > 0:
                    update_gears(lineIndex, columnIndex, int(currentNumber))
                    currentNumber = ""

        if currentNumber != "":
            update_gears(lineIndex, noColumns, int(currentNumber))

    gearSum = 0

    for line in gearSchematic:
        for element in line:
            if element[0] == 2:
                gearSum += element[1]

    print(gearSum)


solve_b()
