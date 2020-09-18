# Non-Exhaustive Recursion Implementation of Crypto-Arithmetic Problem

## Crypt Arithmetic:

Crypt arithmetic, also known as alphametics, cryptarithmetic, or word addition, is a type of mathematical game consisting of a mathematical equation among unknown numbers, whose digits are represented by letters. The goal is to identify the value of each letter. The name can be extended to puzzles that use non-alphabetic symbols instead of letters.

```
 SEND
+MORE
------
MONEY
```

_Figure 1: Example of alphametic problem_

# Pseudocode

Below pseudocode, in this case, has more special cases, but the same general design

-   Start by examining the rightmost digit of the topmost row, with a carry of 0
-   If we are beyond the leftmost digit of the puzzle, return true if no carry, false otherwise
-   If we are currently trying to assign a char in one of the addends
    -   If char already assigned, just recur on the row beneath this one, adding value into the sum
    -   If not assigned, then
        -   for (every possible choice among the digits not in use)
        -   make that choice and then on row beneath this one, if successful, return true
        -   if !successful, unmake assignment and try another digit
    -   return false if no assignment worked to trigger backtracking
-   Else if trying to assign a char in the sum
    -   If char assigned & matches correct,
        -   recur on next column to the left with carry, if success return true,
    -   If char assigned & doesn’t match, return false
    -   If char unassigned & correct digit already used, return false
    -   If char unassigned & correct digit unused,
        -   assign it and recur on next column to left with carry, if success return true
    -   return false to trigger backtracking

## Usage Examples

```
Enter expression: ten+ten+forty=sixty
{'n': 0, 'y': 6, 'e': 5, 't': 8, 'r': 7, 'x': 4, 'o': 9, 'i': 1, 'f': 2, 's': 3}
```

```
Enter expression: send+more=money
{'d': 1, 'e': 5, 'y': 6, 'n': 3, 'r': 2, 'o': 8, 's': 7, 'm': 0}
{'d': 1, 'e': 7, 'y': 8, 'n': 3, 'r': 4, 'o': 6, 's': 5, 'm': 0}
{'d': 1, 'e': 8, 'y': 9, 'n': 2, 'r': 6, 'o': 4, 's': 3, 'm': 0}
{'d': 1, 'e': 8, 'y': 9, 'n': 5, 'r': 3, 'o': 7, 's': 6, 'm': 0}
{'d': 2, 'e': 4, 'y': 6, 'n': 3, 'r': 1, 'o': 9, 's': 8, 'm': 0}
{'d': 2, 'e': 5, 'y': 7, 'n': 4, 'r': 1, 'o': 9, 's': 8, 'm': 0}
{'d': 2, 'e': 7, 'y': 9, 'n': 1, 'r': 6, 'o': 4, 's': 3, 'm': 0}
{'d': 2, 'e': 7, 'y': 9, 'n': 3, 'r': 4, 'o': 6, 's': 5, 'm': 0}
{'d': 3, 'e': 6, 'y': 9, 'n': 4, 'r': 2, 'o': 8, 's': 7, 'm': 0}
{'d': 3, 'e': 8, 'y': 1, 'n': 5, 'r': 2, 'o': 7, 's': 6, 'm': 0}
{'d': 4, 'e': 3, 'y': 7, 'n': 2, 'r': 1, 'o': 9, 's': 8, 'm': 0}
{'d': 4, 'e': 5, 'y': 9, 'n': 2, 'r': 3, 'o': 7, 's': 6, 'm': 0}
{'d': 4, 'e': 5, 'y': 9, 'n': 3, 'r': 2, 'o': 8, 's': 7, 'm': 0}
{'d': 5, 'e': 4, 'y': 9, 'n': 1, 'r': 3, 'o': 7, 's': 6, 'm': 0}
{'d': 6, 'e': 3, 'y': 9, 'n': 1, 'r': 2, 'o': 8, 's': 7, 'm': 0}
{'d': 7, 'e': 5, 'y': 2, 'n': 6, 'r': 8, 'o': 0, 's': 9, 'm': 1}
{'d': 7, 'e': 8, 'y': 5, 'n': 1, 'r': 6, 'o': 3, 's': 2, 'm': 0}
{'d': 9, 'e': 4, 'y': 3, 'n': 1, 'r': 2, 'o': 7, 's': 6, 'm': 0}
{'d': 9, 'e': 4, 'y': 3, 'n': 2, 'r': 1, 'o': 8, 's': 7, 'm': 0}
{'d': 9, 'e': 5, 'y': 4, 'n': 3, 'r': 1, 'o': 8, 's': 7, 'm': 0}
{'d': 9, 'e': 6, 'y': 5, 'n': 4, 'r': 1, 'o': 8, 's': 7, 'm': 0}
{'d': 9, 'e': 7, 'y': 6, 'n': 1, 'r': 5, 'o': 4, 's': 3, 'm': 0}
{'d': 9, 'e': 8, 'y': 7, 'n': 1, 'r': 6, 'o': 3, 's': 2, 'm': 0}
{'d': 9, 'e': 8, 'y': 7, 'n': 2, 'r': 5, 'o': 4, 's': 3, 'm': 0}
{'d': 9, 'e': 8, 'y': 7, 'n': 4, 'r': 3, 'o': 6, 's': 5, 'm': 0}
```
