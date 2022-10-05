#listP = [y for y in range(10 ** 6) if y % 2 != 0 and ( y > 3 and y % 3 != 0) and ( y > 5 and y % 5 != 0)]
#print(listP)
# returns 26297 line long list

def sieve(num):
    listp = [True for i in range(num+1)]
    test = 2
    finalp = []
    while (test*test) <= num:
        if listp[test] == True:
            for i in range((test*test), num+1, test):
                listp[i] = False
        test += 1
    for i in range(2,num+1):
        if listp[i] == True:
            finalp.append(i)
              
    return finalp
#    for test in range(2,num+1):
#        if listp[test]:
#            print(test)

num = 1000
listprimes = [i for i in sieve(num)]
totalSum = 0
bigSum = 0
startnum = 0
count = 0
savedcount = 0
end = 0
while startnum < (len(listprimes) - end):
    for i in range(startnum, (len(listprimes) - end), -1):
        count += 1
        totalSum += listprimes[i]
        if (totalSum < num) and (totalSum in listprimes):
            if totalSum > bigSum and count > savedcount:
                bigSum = totalSum
                savedcount = count
        elif (totalSum > bigSum) and count < savedcount:
            totalSum = 0
            count = 0
            break
    totalSum = 0
    count = 0
    end += 1
print(bigSum)

        
        
