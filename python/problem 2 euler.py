num = 0
current = 1
currentMinusOne = 1
currentMinusTwo = 1
while current < 4000000:
    if (current % 2) == 0:
        num += current
    current = currentMinusOne + currentMinusTwo
    currentMinusTwo = currentMinusOne
    currentMinusOne = current
print(num)
