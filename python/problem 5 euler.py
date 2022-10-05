totalR = 1
testnum = 8680
while totalR != 0:
    for i in range(20,0,-1):
        if testnum % i != 0:
            testnum += 20
            break
        elif i == 1:
            totalR = 0
            print(str(testnum) + 'is answer')

    
