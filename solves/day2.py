fileName = "day2input.txt"
originalColors = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(game: str):
    seenColors = dict()
    info = game.strip().split(":")[1]
    reveals = info.split(";")
    for reveal in reveals:

        colors = reveal.split(",")
        for color in colors:

            value, currentColor = color.strip().split(" ")
            value = int(value)

            valueBefore = seenColors.setdefault(currentColor, value)
            if valueBefore < value:
                seenColors[currentColor] = value

    for color in originalColors.keys():
        if originalColors.get(color) < seenColors.get(color, 0):
            return False
    return True


def solve_a():
    myFile = open(fileName, "r")
    games = myFile.readlines()
    idxSum = 0

    for idx, game in enumerate(games):
        idxSum += idx+1 if is_possible(game) else 0

    print(idxSum)


def power_number(game: str):
    seenColors = dict()
    info = game.strip().split(":")[1]
    reveals = info.split(";")
    for reveal in reveals:

        colors = reveal.split(",")
        for color in colors:

            value, currentColor = color.strip().split(" ")
            value = int(value)

            valueBefore = seenColors.setdefault(currentColor, value)
            if valueBefore < value:
                seenColors[currentColor] = value

    result = 1
    for color in seenColors.keys():
        result *= seenColors[color]

    return result


def solve_b():
    myFile = open(fileName, "r")
    games = myFile.readlines()
    idxSum = 0

    for idx, game in enumerate(games):
        idxSum += power_number(game)

    print(idxSum)

solve_b()
