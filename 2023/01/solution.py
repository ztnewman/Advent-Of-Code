#!/usr/bin/env python3

f = open("input.txt")

total = 0
first = list()
last = list()
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in f:
    for char in line:
        if char.isdigit():
            if len(first) == 0:
                first.append(char)
                last.append(char)
            else:
                last.append(char)

    for digit in digits:
        if digit in line:
            if len(first) == 0:
                first.append(digits.index(digit))
            elif line.index(digit) < line.index(str(first[0])):
                first.append(digits.index(digit))

            if len(last) == 0:
                last.append(digits.index(digit))
            elif line.index(digit) > line.index(str(last[-1])):
                last.append(digits.index(digit))

    total = total + int(first.pop()) + int(last.pop())
    first = list()
    last = list()

print(total)
