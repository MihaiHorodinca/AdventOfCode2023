import math

fileName = "day6input.txt"
myFile = open(fileName, "r")
textInput = myFile.readlines()


def solve_a():
    times = [int(number) for number in textInput[0].split(":")[1].strip().split()]
    distances = [int(number) for number in textInput[1].split(":")[1].strip().split()]

    totalWinningSituations = 1
    for index, raceTime in enumerate(times):
        currentWinningPossibilities = 0
        raceDistance = distances[index]

        delta = raceTime * raceTime - 4 * raceDistance

        solution1 = ((-raceTime) + (math.sqrt(delta))) / (-2)
        solution2 = ((-raceTime) - (math.sqrt(delta))) / (-2)

        print(solution1)
        print(solution2)

        currentWinningPossibilities = math.floor(solution2) - math.ceil(solution1) + 1
        if int(solution2) == solution2:
            currentWinningPossibilities -= 1
        if int(solution1) == solution1:
            currentWinningPossibilities -= 1

        totalWinningSituations *= currentWinningPossibilities
        print(currentWinningPossibilities)

    print(totalWinningSituations)


def solve_b():
    raceTimeParts = textInput[0].split(":")[1].strip().split()
    raceTime = int("".join(raceTimeParts))

    raceDistanceParts = textInput[1].split(":")[1].strip().split()
    raceDistance = int("".join(raceDistanceParts))

    delta = raceTime * raceTime - 4 * raceDistance

    solution1 = ((-raceTime) + (math.sqrt(delta))) / (-2)
    solution2 = ((-raceTime) - (math.sqrt(delta))) / (-2)

    print(solution1)
    print(solution2)

    currentWinningPossibilities = math.floor(solution2) - math.ceil(solution1) + 1
    if int(solution2) == solution2:
        currentWinningPossibilities -= 1
    if int(solution1) == solution1:
        currentWinningPossibilities -= 1

    print(currentWinningPossibilities)


solve_b()
