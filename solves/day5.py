fileName = "day5input.txt"
myFile = open(fileName, "r")
myInput = myFile.readlines()


class SourceRange:
    def __init__(self, start, length, changed=False):
        self.start = start
        self.length = length
        self.changed = changed

    def unchange(self):
        self.changed = False


def transform(seeds: [int], transformations):
    changed = [False] * len(seeds)
    for transformation in transformations:
        destinationStart, sourceStart, rangeLength = [int(x) for x in transformation.split()]
        change = destinationStart - sourceStart
        print(f"From: {sourceStart} To: {destinationStart} Changing: {change} For: {rangeLength}")
        for index, seed in enumerate(seeds):
            if not changed[index] and sourceStart <= seed < sourceStart + rangeLength:
                seeds[index] = seed + change
                changed[index] = True
        print(f"Resulting values: {seeds}")


def transform_ranges(sourceRanges: [SourceRange], transformations: [str]):
    for transformation in transformations:
        transformationDestinationStart, transformationSourceStart, rangeLength = [int(x) for x in transformation.split()]
        change = transformationDestinationStart - transformationSourceStart
        transformationSourceFinish = transformationSourceStart + rangeLength

        for index, sourceRange in enumerate(sourceRanges):
            if sourceRange.changed:
                continue

            if transformationSourceFinish <= sourceRange.start or sourceRange.start + sourceRange.length < transformationSourceStart:
                continue

            if transformationSourceStart >= sourceRange.start and transformationSourceFinish <= sourceRange.start + sourceRange.length:
                sourceRanges[index] = SourceRange(transformationDestinationStart, rangeLength, True)
                sourceRanges.append(SourceRange(sourceRange.start, transformationSourceStart - sourceRange.start))
                sourceRanges.append(SourceRange(transformationSourceFinish, sourceRange.start + sourceRange.length - transformationSourceFinish))
                continue

            if transformationSourceStart > sourceRange.start:
                sourceRanges[index] = SourceRange(sourceRange.start, transformationSourceStart - sourceRange.start)
                sourceRanges.append(SourceRange(transformationDestinationStart, transformationDestinationStart + sourceRange.start + sourceRange.length - transformationSourceStart, True))
                continue

            if transformationSourceFinish < sourceRange.start + sourceRange.length:
                sourceRanges[index] = SourceRange(transformationSourceFinish, sourceRange.length - (transformationSourceFinish - sourceRange.start))
                sourceRanges.append(SourceRange(transformationDestinationStart, transformationSourceFinish - sourceRange.start, True))

        for sourceRange in sourceRanges:
            sourceRange.unchange()


def get_seeds(textSeeds: str):
    return [int(seed) for seed in textSeeds.split()]


def get_seeds_ranges(textSeeds: str):
    return [SourceRange(int(number), int(length)) for index, number in textSeeds.split() if index%2 == 0]


def solve_a():
    textSeeds = myInput[0].split(":")[1]
    seeds = get_seeds(textSeeds)
    print(seeds)
    textTransformations = myInput[2:] + ['\n']

    inTransformation = False
    currentTransformations = []
    for line in textTransformations:
        if ":" in line:
            print()
            print(line)
            inTransformation = True
            continue

        if inTransformation:
            currentTransformations.append(line)

        if line.strip() == "":
            print("NEW TRANSFORMATIONS")
            transform(seeds, currentTransformations[:-1])
            currentTransformations = []
            inTransformation = False

    print(min(seeds))


def solve_b():
    textSeedRanges = myInput[0].split(":")[1]
    sourceRanges = get_seeds_ranges(textSeedRanges)
    print([[sourceRange.start, sourceRange.length] for sourceRange in sourceRanges])
    textTransformations = myInput[2:] + ['\n']

    inTransformation = False
    currentTransformations = []
    for line in textTransformations:
        if ":" in line:
            print()
            print(line)
            inTransformation = True
            continue

        if inTransformation:
            currentTransformations.append(line)

        if line.strip() == "":
            print("NEW TRANSFORMATIONS")
            transform_ranges(sourceRanges, currentTransformations[:-1])
            currentTransformations = []
            inTransformation = False
    print(min([sourceRange.start for sourceRange in sourceRanges]))


solve_b()
