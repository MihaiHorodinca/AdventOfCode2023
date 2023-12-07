def get_calibration_number(calibrationLine):
    digits = [char for char in calibrationLine if char.isdigit()]
    return int(digits[0]) * 10 + int(digits[-1])


def solve_a():
    calibrationSum = 0
    myFile = open("day1input.txt", "r")
    calibrations = myFile.readlines()

    for calibrationLine in calibrations:
        calibrationSum += get_calibration_number(calibrationLine)

    print(calibrationSum)


digits_spelled_out = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_calibration_number_with_spelled_digits(calibrationLine: str):
    # check all digits
    digits = [(idx, int(val)) for (idx, val) in enumerate(calibrationLine) if val.isdigit()]

    if len(digits) == 0:
        firstCalibrationIdx = len(calibrationLine)
        firstCalibrationVal = -1
        lastCalibrationIdx = -1
        lastCalibrationVal = -1
    else:
        firstCalibrationIdx = digits[0][0]
        firstCalibrationVal = digits[0][1]
        lastCalibrationIdx = digits[-1][0]
        lastCalibrationVal = digits[-1][1]

    for spellingIdx, spelling in enumerate(digits_spelled_out):
        firstIdx = calibrationLine.find(spelling)
        lastIdx = calibrationLine.rfind(spelling)

        if firstIdx == -1:
            continue

        if firstIdx < firstCalibrationIdx:
            firstCalibrationIdx = firstIdx
            firstCalibrationVal = spellingIdx

        if lastIdx > lastCalibrationIdx:
            lastCalibrationIdx = lastIdx
            lastCalibrationVal = spellingIdx

    return firstCalibrationVal * 10 + lastCalibrationVal


def solve_b():
    calibrationSum = 0
    myFile = open("day1input.txt", "r")
    calibrations = myFile.readlines()

    for calibrationLine in calibrations:
        calibrationSum += get_calibration_number_with_spelled_digits(calibrationLine)

    print(calibrationSum)


solve_b()
