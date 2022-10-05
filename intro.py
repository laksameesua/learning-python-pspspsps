# + addition 
# - subtraction
# * multiplication
# / division
# % modulus, finds the remainder when x is divided by y
# ** exponentiation
# // floor division
final = 0
setOfMuls = {0}
for i in range(335):
    mul_3 = 3*i
    mul_5 = 5*i
    if mul_3 < 1000:
        setOfMuls.add(mul_3)
    if mul_5 < 1000:
        setOfMuls.add(mul_5)
for i in setOfMuls:
    final += i
print(final)
#print(i)
#print(mul_3)
#print(mul_5)
