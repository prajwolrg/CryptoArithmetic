strAddends = []
strSum = ""


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
    unassignedDigits = [i for i in range(10)]
    solveIter({}, unassignedDigits, 0, 0, 0)


solve("send+more=money")

