Counter = 100

while True:
    if all(Counter % i == 0 for i in range(1, 21)):
        break
    Counter += 1

print("the answer is: ",Counter)
