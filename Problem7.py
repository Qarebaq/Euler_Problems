Prime = 2
Counter = 3
Prime_Counter = 1

while Prime_Counter <10001 :
    is_Prime  = True
    for i in range(2,int(Counter**0.5)+1):
        if Counter % i == 0:
            is_Prime = False
            break

    if is_Prime:
        Prime_Counter += 1
        Prime = Counter
    Counter += 1
         
print("The 10 001th prime number is: ", Prime)