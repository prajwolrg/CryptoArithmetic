strAddends = []
strSum = ""


def checkSumValue(values, index):
    sumValue = 0
    for k in range(len(strAddends)):
        if index <= len(strAddends[k]):
            sumValue += values[strAddends[k][-index]]
    statement = "checksum value for index " + str(index) + " is" + str(sumValue)
    print(statement)

    if values[strSum[-index]] == sumValue % 10:
        return True

    return False


def generateValue(values, key):
    for i in range(10):
        if checkValue(values, key, i):
            print("generating value for ", key, i)
            values[key] = i
            return i


def choice(values, index):
    for k in range(len(strAddends)):
        if len(strAddends[k]) >= index + 1:
            generateValue(values, strAddends[k][i])
    if checkSumValue(values, i):
        solveIter(values, index + 1)


def checkValue(values, key, value):
    # Check the previous values for reptition
    if values[key] == value:
        return True
    index = list(values.keys()).index(key)
    for i in range(index):
        if values[list(values.keys())[i]] == value:
            # print([list(values.keys())[i]], "has the same value as ", key)
            return False
    return True


def addend(row):
    if row < len(strAddends):
        return True
    else:
        return False


def assigned(solution, row, col):
    if addend(row):
        if len(strAddends[row]) > col:
            if strAddends[row][-col - 1] in solution:
                return True
    else:
        if strSum[-col - 1] in solution:
            return True
    return False


def match(solution, sum, col):
    if solution[strSum[-col - 1]] == sum % 10:
        return True
    else:
        return False


def used(unassignedDigits, digit):
    if digit not in unassignedDigits:
        return True
    else:
        return False


def assign(solution, unassignedDigits, row, col, value):
    if addend(row):
        solution[strAddends[row][-col - 1]] = value
    else:
        solution[strSum[-col - 1]] = value
    unassignedDigits.remove(value)
    return [solution, unassignedDigits]


def unassign(solution, unassignedDigits, row, col):
    if addend(row):
        value = solution[strAddends[row][-col - 1]]
        solution.pop(strAddends[row][-col - 1])
    else:
        value = solution[strSum[-col - 1]]
        solution.pop(strSum[-col - 1])
    unassignedDigits.append(value)
    unassignedDigits.sort()
    return [solution, unassignedDigits]


def genSum(solution, col, carry):
    sum = carry
    for i in range(len(strAddends)):
        if exists(i, col):
            sum += solution[strAddends[i][-col - 1]]
    return sum


def exists(row, col):
    if len(strAddends[row]) > col:
        return True
    else:
        return False


def solveIter(solution, unassignedDigits, row, col, carry):
    # print(solution)
    # print(unassignedDigits)
    # print()
    if col >= len(strSum):
        print(solution)
        return True

    sum = carry
    if addend(row):
        if exists(row, col):
            if assigned(solution, row, col):
                # print(strAddends[row][-col - 1], "is already assigned")
                solveIter(solution, unassignedDigits, row + 1, col, carry)
            else:
                for i in unassignedDigits:
                    [solution, newunassignedDigits] = assign(
                        solution, unassignedDigits, row, col, i
                    )
                    if solveIter(solution, newunassignedDigits, row + 1, col, carry):
                        return True
                    else:
                        [solution, unassignedDigits] = unassign(
                            solution, unassignedDigits, row, col
                        )
                return False
        else:
            solveIter(solution, unassignedDigits, row + 1, col, carry)

    else:
        sum = genSum(solution, col, carry)
        carry = sum // 10
        if assigned(solution, row, col) and match(solution, sum, col):
            # print("assigned and matches")
            if solveIter(solution, unassignedDigits, 0, col + 1, carry):
                return True

        if assigned(solution, row, col) and not match(solution, sum, col):
            # print("assigned and do not match")
            return False

        if not assigned(solution, row, col) and used(unassignedDigits, sum % 10):
            # print("not assigned but used")
            return False

        if not assigned(solution, row, col) and not used(unassignedDigits, sum % 10):
            # print("Not assigned not used")
            [newSolution, newUnassignedDigits] = assign(
                solution, unassignedDigits, row, col, sum % 10
            )
            if solveIter(solution, unassignedDigits, 0, col + 1, carry):
                return True
            else:
                [solution, unassignedDigits] = unassign(
                    solution, unassignedDigits, row, col
                )

    return False


def solve(expression):
    values = initialValues(expression)
    unassignedDigits = [i for i in range(10)]
    solveIter({}, unassignedDigits, 0, 0, 0)


def initialValues(expression):
    values = {}
    global strAddends
    global strSum
    [strAddends, strSum] = expression.split("=")
    strAddends = strAddends.split("+")
    strAddends.sort(key=len)

    for k in range(len(strAddends)):
        for i in range(-1, -len(strAddends[k]) - 1, -1):
            for j in range(k, len(strAddends)):
                if strAddends[j][i] not in values:
                    values[strAddends[j][i]] = -1
            if strSum[i] not in values:
                values[strSum[i]] = -1

    for k in range(-len(strAddends[-1]), -len(strSum) - 1, -1):
        if strSum[k] not in values:
            values[strSum[k]] = -1

    return values


solve("send+more=money")
# checkValue(values, "n", -1)

