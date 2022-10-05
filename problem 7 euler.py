test = 3
setofprimes = [2]
done = 1
while done != 10001:
    for i in setofprimes:
        if test % i == 0:
            test += 2
            break
        elif i == setofprimes[-1]:
            setofprimes.append(test)
            done += 1
            test += 2
            break
print(test - 2)

        
