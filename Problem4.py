def is_Palindrome(num):
    temp1 = int(num)
    temp = int(num) 
    Answer = int(num)
    n = 0
    Check = 0 
    while num> 0:
        num = num // 10
        n = n + 1
    arr = [0] * n
    arrtst = [0] * n
    for i in range(0,n):
        arr[i]  = temp %10 
        temp = int(temp // 10)
    for j in range(n-1,-1,-1):
        arrtst[j] = temp1 % 10
        temp1 = int(temp1 // 10)
    for i in range(0,n):
        if (arr[i] == arrtst[i]):
            Check = Check + 1
    if (Check == n):
        Check_is_this_Big(Answer)

def Check_is_this_Big(answer):
    global Biggest_palindrome  
    if answer > Biggest_palindrome:
        Biggest_palindrome = answer


Biggest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_Palindrome(product) and product > Biggest_palindrome:
            Biggest_palindrome = product

print("The biggest palindrome is:", Biggest_palindrome)
