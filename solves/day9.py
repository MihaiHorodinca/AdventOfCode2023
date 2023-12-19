def get_input():
    fileName = "day9input.txt"
    myFile = open(fileName, 'r')

    return [[int(number) for number in line.split()] for line in myFile.readlines()]


def solve_history(history: [int]):
    if all(number == 0 for number in history):
        return 0

    newHistory = [number - history[index - 1] for index, number in enumerate(history, 0) if index != 0]
    return solve_history(newHistory) + history[-1]


def solve_history_backwards(history: [int]):
    if all(number == 0 for number in history):
        return 0

    newHistory = [number - history[index - 1] for index, number in enumerate(history, 0) if index != 0]
    return history[0] - solve_history_backwards(newHistory)


def solve_a():
    histories = get_input()

    solutions = [solve_history_backwards(history) for history in histories]

    print(solutions)
    print(sum(solutions))


solve_a()
