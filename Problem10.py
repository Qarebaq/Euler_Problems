sum =0

for i in range (2,2000000):
    is_Prime = True
    for j in range (2,int(i**0.5)+1):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime:
        sum += i


print("The sum of all prime numbers below 10 is: ", sum)