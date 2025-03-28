counter1 = 1
counter2 = 0
sum1 = 0
sum2 =0 

for i in range (1,101):
    counter1 = i * i
    sum1 = sum1 + counter1

for i in range (1,101):
    counter2 = i + counter2


sum2 = counter2 * counter2

print ("The answer is: ", (sum2 - sum1))