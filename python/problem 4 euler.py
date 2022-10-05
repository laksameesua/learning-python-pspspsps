num1 = 999
num2 = 999
mun = 0
bignum = 0

while num1 != 0:
    num = num1 * num2
    mun = 0
    while num != 0:
        mun = mun * 10 + num % 10
        num = (num - num % 10) / 10
    if num1 * num2 == mun and mun > bignum:
        bignum = mun
        if num2 != 0:
            num2 -= 1
        else:
            num1 -=1
    elif num2 != 0:
        num2 -= 1
    else:
        num1 -= 1
        num2 = num1
print(bignum)
