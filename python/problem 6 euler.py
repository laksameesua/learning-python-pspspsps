totalsum = 0
given = 100
for i in range (0,given + 1):
    totalsum += i**2
totalsq = ((given+1) * (given/2)) ** 2
print(totalsq)
print(totalsq - totalsum)

