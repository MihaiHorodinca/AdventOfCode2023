import re


def solve_a():
    f = open("scratchcards.txt", "r")
    cards = f.readlines()
    totalScore = 0

    for line in cards:
        totalScore += solve_card(line)
        print(totalScore)


def solve_card(line):
    numbers = re.findall(r'\d+', line)
    noWinning = 10
    winningNumbers = numbers[1:1+noWinning]
    myNumbers = numbers[noWinning+1:]
    score = 0
    for _ in filter(lambda number: winningNumbers.__contains__(number), myNumbers):
        score += 1
    return score


def solve_b():
    f = open("scratchcards.txt", "r")
    cards = f.readlines()
    counters = [0] * 250
    currentStack = 1
    totalScratched = 0

    for index, line in enumerate(cards):
        currentStack += counters[index]
        totalScratched += currentStack

        extraCards = solve_card(line)
        counters[index+1] += currentStack
        counters[min(index+1+extraCards, 245)] -= currentStack
        print(totalScratched)


if __name__ == '__main__':
    solve_b()
