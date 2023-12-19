import math

def parse_line(line):
    name = line[:3]
    left = line[7:10]
    right = line[12:15]
    return name, left, right


def get_input():
    fileName = "day8input.txt"
    myFile = open(fileName, "r")
    myInput = myFile.readlines()

    instructions = myInput[0].strip()
    nodes = {name: (left, right) for name, left, right in [parse_line(line) for line in myInput[2:]]}

    return instructions, nodes


def solve():
    instructions, nodes = get_input()

    currentNodes = [name for name in nodes.keys() if name.endswith('A')]
    stepCount = 0
    instructionIndex = 0

    while True:
        for index, currentNode in enumerate(currentNodes):
            step = instructions[instructionIndex]

            if step == "L":
                currentNodes[index] = nodes.get(currentNode)[0]
            else:
                currentNodes[index] = nodes.get(currentNode)[1]

        stepCount += 1
        instructionIndex += 1
        if instructionIndex == len(instructions):
            instructionIndex = 0

        if all(name.endswith('Z') for name in currentNodes):
            break

        if stepCount % 1000000 == 0:
            print(stepCount)

    print(stepCount)


def get_cycle_length(start: str, instructions: str, nodes: {str: (str, str)}):
    currentNode = start
    stepCount = 0
    instructionIndex = 0

    while True:
        step = instructions[instructionIndex]

        if step == "L":
            currentNode = nodes.get(currentNode)[0]
        else:
            currentNode = nodes.get(currentNode)[1]

        stepCount += 1
        instructionIndex += 1
        if instructionIndex == len(instructions):
            instructionIndex = 0

        if currentNode.endswith('Z'):
            return stepCount


def solve_efficient():
    instructions, nodes = get_input()

    starts = [name for name in nodes.keys() if name.endswith('A')]
    print(len(starts))
    cycles = [get_cycle_length(start, instructions, nodes) for start in starts]

    print(math.lcm(*cycles))


solve_efficient()
