fileName = "day11input.txt"
myFile = open(fileName, 'r')

galaxies = []
rowGaps = []
columnGaps = []


def get_input():
    global rowGaps
    global columnGaps

    text = myFile.readlines()
    rowGaps = [a for a in range(0, len(text))]
    columnGaps = [a for a in range(0, len(text[0])-1)]

    for rowIndex, row in enumerate(text):
        for columnIndex, char in enumerate(row):
            if char == "#":
                galaxies.append((rowIndex, columnIndex))
                if rowIndex in rowGaps:
                    rowGaps.remove(rowIndex)
                if columnIndex in columnGaps:
                    columnGaps.remove(columnIndex)

    print(rowGaps)
    print(columnGaps)
    print(galaxies)


def is_gap_between(gap, v1, v2):
    return v1 < gap < v2 or v1 > gap > v2


def distance_between_galaxies(galaxy1, galaxy2):
    noRowGaps = len([gap for gap in rowGaps if is_gap_between(gap, galaxy1[0], galaxy2[0])])
    noColumnGaps = len([gap for gap in columnGaps if is_gap_between(gap, galaxy1[1], galaxy2[1])])
    rowDiff = abs(galaxy1[0] - galaxy2[0]) + noRowGaps * 999999
    columnDiff = abs(galaxy1[1] - galaxy2[1]) + noColumnGaps * 999999

    # print(f'Found distance {rowDiff + columnDiff} between {galaxy1} and {galaxy2} with {noRowGaps} rowGaps and {noColumnGaps} columnGaps')

    return rowDiff + columnDiff


def solve_a():
    total = 0
    count = 0
    for g1Idx, galaxy1 in enumerate(galaxies):
        for g2Idx, galaxy2 in enumerate(galaxies):
            if g1Idx < g2Idx:
                count += 1
                total += distance_between_galaxies(galaxy1, galaxy2)

    print(total)
    print(count)


get_input()
solve_a()
