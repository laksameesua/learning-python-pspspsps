storedX = 0
goal = 600851475143
setOfFactors = {0}
x = 2
while x <= goal:
    if goal % x == 0:
        goal = goal / x
        setOfFactors.add(x)
    else:
        x+=1
print(setOfFactors)
