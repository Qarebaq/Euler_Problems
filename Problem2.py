def fib(n):
    if (n==1):
        return 1
    if(n ==2):
        return 2
    else:
        return fib(n-1) + fib(n-2)
n= 1
sum = 0

while(fib(n)<4000000):
    n = n +1
    if(fib(n)%2==0):
        sum = sum + fib(n)


print("the sum of even fibonacci numbers less than 4 million is: ", sum)